from typing import TYPE_CHECKING

from django.db.models import Q, QuerySet
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from server.pagination import StandardResultsSetPagination
from inventory.models import Release, Track
from inventory.serializers import ReleaseSerializer, TrackSerializer

if TYPE_CHECKING:
    ReleaseModelViewset = ModelViewSet[Release]
    TrackModelViewset = ModelViewSet[Track]
else:
    ReleaseModelViewset = ModelViewSet
    TrackModelViewset = ModelViewSet


class ReleaseViewset(ReleaseModelViewset):
    description = "CRUD operations on album releases."
    pagination_class = StandardResultsSetPagination
    serializer_class = ReleaseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["artist_name", "album_title", "genre"]

    def get_queryset(self) -> QuerySet:
        filters = Q()
        query_params = self.request.query_params

        genre = query_params.get("genre", None)
        if genre:
            filters &= Q(genre__icontains=genre)

        artist = query_params.get("artist", None)
        if artist:
            filters &= Q(artist_name__icontains=artist)

        album = query_params.get("album", None)
        if album:
            filters &= Q(album_title__icontains=album)

        return Release.objects.filter(filters).order_by("artist_name")


class TrackViewSet(TrackModelViewset):
    description = "CRUD operations on album tracks."
    serializer_class = TrackSerializer

    def get_queryset(self) -> QuerySet:
        return Track.objects.all()
