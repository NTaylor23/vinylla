from typing import List
from rest_framework import serializers

from inventory.models import Release, Track


class ReleaseSerializer(serializers.ModelSerializer["Release"]):
    formatted_name: serializers.SerializerMethodField = (
        serializers.SerializerMethodField()
    )
    tracks: serializers.SerializerMethodField = serializers.SerializerMethodField()

    class Meta:
        model = Release
        fields = [
            "pk",
            "artist_name",
            "formatted_name",
            "album_title",
            "genre",
            "style",
            "format",
            "discogs_release_id",
            "year",
            "price",
            "in_wantlist",
            "image_url",
            "thumbnail_url",
            "tracks",
        ]

    def get_formatted_name(self, instance: Release) -> str:
        name: str = instance.artist_name
        if name.endswith(")"):
            sp = name.split(" ")
            sp.pop()
            return " ".join(sp)
        return name

    def get_tracks(self, instance: Release) -> List[Track]:
        data = instance.track_set.all()
        serialized = TrackSerializer(data, many=True)
        return serialized.data


class TrackSerializer(serializers.ModelSerializer["Track"]):
    class Meta:
        model = Track
        fields = ["release", "track_title", "duration"]
