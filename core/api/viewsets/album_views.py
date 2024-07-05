from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from core.api.serializers import AlbumListStringRelatedFieldSerializer
from core.models import Album


class AlbumListRetrieve(viewsets.ReadOnlyModelViewSet):
    queryset = Album.objects.all().select_related("band")
    serializer_class = AlbumListStringRelatedFieldSerializer
    permission_classes = [IsAdminUser]
