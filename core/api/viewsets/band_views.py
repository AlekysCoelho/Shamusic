from rest_framework import mixins, viewsets

from core.api.serializers import BandSerializer
from core.models import Band


class BandViewsets(viewsets.ModelViewSet):
    queryset = Band.objects.all()
    serializer_class = BandSerializer


class BandListViewsets(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Band.objects.all()
    serializer_class = Band
