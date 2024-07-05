from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from core.api.viewsets import AlbumListRetrieve, BandListViewsets, BandViewsets
from core.api.viewsets.musician_views import MusiciansViewsets
from core.api.viewsets.track_views import TracksListRetrieve, TracksViewsets

router = routers.DefaultRouter()

# ALBUM
router.register(r"albums", AlbumListRetrieve, basename="albums")

# BAND
router.register(r"bands", BandViewsets, basename="bands")
# router.register(r"bands-list", BandListViewsets, basename="bands-list")

# MUSICIAN
router.register(r"musicians", MusiciansViewsets, basename="musicians")

# TRACK
router.register(r"tracks", TracksViewsets, basename="tracks")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-admin/", include(router.urls)),
    # path("shaplayer/", include(("core.urls", "shaplayer"), namespace="shaplayer")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
