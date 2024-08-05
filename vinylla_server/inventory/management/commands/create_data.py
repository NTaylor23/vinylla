from typing import Any, Union

from django.core.management.base import BaseCommand
from inventory.models import Release, Track

import json


def parse_with_fallback(
    data: dict, key: Union[int, str], default: Union[int, str]
) -> Any:
    try:
        return data[key]
    except Exception:
        return default


class Command(BaseCommand):
    help = "Pull release information from Discogs to populate the API."

    def handle(self, *args: Any, **options: Any) -> None:
        if Release.objects.count() == 0:
            with open("data.json", "r") as jsonfile:
                data = json.load(jsonfile)
            try:
                for release in data:
                    basic_information = release["basic_information"]
                    d = {
                        "album_title": parse_with_fallback(
                            basic_information, "title", "[No Title]"
                        ),
                        "artist_name": parse_with_fallback(
                            basic_information["artists"][0], "name", "[No Artist Name]"
                        ),
                        "genre": parse_with_fallback(
                            basic_information["genres"], 0, "[No Genre]"
                        ),
                        "style": parse_with_fallback(
                            basic_information["styles"], 0, "[No Style]"
                        ),
                        "format": parse_with_fallback(
                            basic_information["formats"][0], "name", "[No Format]"
                        ),
                        "discogs_release_id": parse_with_fallback(release, "id", 0),
                        "year": parse_with_fallback(basic_information, "year", 0),
                        "price": 10.00,
                        "image_url": parse_with_fallback(
                            basic_information, "cover_image", "[No Cover Image]"
                        ),
                        "thumbnail_url": parse_with_fallback(
                            basic_information, "thumb", "[No Thumbnail]"
                        ),
                    }
                    release_object = Release.objects.create(**d)
                    for track in release["tracklist"]:
                        Track.objects.create(
                            release=release_object,
                            track_title=track["title"],
                            duration=track["duration"],
                        )
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error: {e}"))
                raise
            self.stdout.write(self.style.SUCCESS("Done."))
