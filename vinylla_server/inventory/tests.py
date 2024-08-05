from django.test import TestCase
from inventory.models import Release, Track
from rest_framework import status
from rest_framework.reverse import reverse

import json


class ReleaseTestCase(TestCase):
    def setUp(self) -> None:
        self.test_release_data = {
            "artist_name": "TestArtist",
            "album_title": "TestAlbumTitle",
            "genre": "TestGenre",
            "style": "TestStyle",
            "format": "Vinyl",
            "discogs_release_id": 123,
            "year": 1998,
            "price": 24.99,
        }
        self.test_track_data = {
            "track_title": "TestTitle",
            "duration": "4:33",
        }

    def test_remove_artist_numerator(self) -> None:
        data = self.test_release_data.copy()
        data["artist_name"] = "Test Artist (2)"
        url = reverse("inventory:release-list")
        post_response = self.client.post(
            url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Release.objects.count(), 1)

        get_response = self.client.get(url)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            get_response.json()["results"][0]["formatted_name"], "Test Artist"
        )

    def test_add_tracks(self) -> None:
        url = reverse("inventory:release-list")
        post_response = self.client.post(
            url, json.dumps(self.test_release_data), content_type="application/json"
        )
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Release.objects.count(), 1)
        release = Release.objects.first()

        for duration, track_title in [("1:00", "A"), ("2:00", "B"), ("3:00", "C")]:
            Track.objects.create(
                duration=duration, track_title=track_title, release=release
            )

        get_response = self.client.get(url)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            get_response.json()["results"][0]["tracks"],
            [
                {"duration": "1:00", "release": 1, "track_title": "A"},
                {"duration": "2:00", "release": 1, "track_title": "B"},
                {"duration": "3:00", "release": 1, "track_title": "C"},
            ],
        )
