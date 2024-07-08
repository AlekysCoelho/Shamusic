from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated

from core.api.serializers import (
    AlbumListStringRelatedFieldSerializer,
    BandSerializer,
    MusicianSerializer,
    TrackSerializer,
)
from core.models import Album, Band, Musician, Track


# BAND
class ListBand(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [DjangoModelPermissions]

    def get(self, request, *args, **kwargs):
        """Get all bands."""
        return self.list(request, *args, **kwargs)


class RetrieveBand(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    lookup_field = "id"
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [DjangoModelPermissions]

    def get(self, request, *args, **kwargs):
        """Get only band"""
        return self.retrieve(request, *args, **kwargs)


# ALBUM
class ListAlbum(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Album.objects.all().select_related("band")
    serializer_class = AlbumListStringRelatedFieldSerializer
    permission_classes = [DjangoModelPermissions]

    def get(self, request, *args, **kwargs):
        """Get all albums."""
        return self.list(request, *args, **kwargs)


class RetrieveAlbum(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    lookup_field = "id"
    queryset = Album.objects.all().select_related("band")
    serializer_class = AlbumListStringRelatedFieldSerializer
    permission_classes = [DjangoModelPermissions]

    def get(self, request, *args, **kwargs):
        """Get only album."""
        return self.retrieve(request, *args, **kwargs)


# MUSICIAN
class ListMusician(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Musician.objects.all().select_related("band")
    serializer_class = MusicianSerializer
    permission_classes = [DjangoModelPermissions]

    def get(self, request, *args, **kwargs):
        """Get all musicians."""
        return self.list(request, *args, **kwargs)


class RetrieveMusician(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    lookup_field = "id"
    queryset = Musician.objects.all().select_related("band")
    serializer_class = MusicianSerializer
    permission_classes = [DjangoModelPermissions]

    def get(self, request, *args, **kwargs):
        """Get only musician."""
        return self.retrieve(request, *args, **kwargs)


# TRACK
class ListTrack(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = (
        Track.objects.all().select_related("album").prefetch_related("by_composers")
    )
    serializer_class = TrackSerializer
    permission_classes = [DjangoModelPermissions]

    def get(self, request, *args, **kwargs):
        """Get all tracks."""
        return self.list(request, *args, **kwargs)


class RetrieveTrack(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    lookup_field = "id"
    permission_classes = [DjangoModelPermissions]
    queryset = (
        Track.objects.all().select_related("album").prefetch_related("by_composers")
    )
    serializer_class = TrackSerializer

    def get(self, request, *args, **kwargs):
        """Get only track."""
        return self.retrieve(request, *args, **kwargs)
