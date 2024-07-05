from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser

from core.api.serializers import BandSerializer
from core.models import Band


class BandViewsets(viewsets.ModelViewSet):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [IsAdminUser]


class BandListViewsets(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Band.objects.all()
    serializer_class = Band
