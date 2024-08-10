from django.urls import include, path
from rest_framework import routers

from inventory.views import ReleaseViewset, TrackViewSet

app_name = "inventory"


router = routers.SimpleRouter()
router.register(r"releases", ReleaseViewset, basename="release")
router.register(r"tracks", TrackViewSet, basename="track")

urlpatterns = [
    path(r"", include(router.urls)),
]
