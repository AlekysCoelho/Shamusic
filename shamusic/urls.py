from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from core.api.viewsets import AlbumListRetrieve, BandListViewsets, BandViewsets

router = routers.DefaultRouter()

# ALBUM
router.register(r"albums-list", AlbumListRetrieve, basename="albums-list")

# BAND
router.register(r"bands", BandViewsets, basename="bands")
router.register(r"bands-list", BandListViewsets, basename="bands-list")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    # path("shaplayer/", include(("core.urls", "shaplayer"), namespace="shaplayer")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
