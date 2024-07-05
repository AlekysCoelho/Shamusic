from rest_framework import mixins, viewsets

from core.api.serializers import TrackSerializer
from core.models import Track


class TracksViewsets(viewsets.ModelViewSet):

    queryset = (
        Track.objects.all().select_related("album").prefetch_related("by_composers")
    )
    serializer_class = TrackSerializer


class TracksListRetrieve(viewsets.ReadOnlyModelViewSet):

    queryset = (
        Track.objects.all().select_related("album").prefetch_related("by_composers")
    )
    serializer_class = TrackSerializer
