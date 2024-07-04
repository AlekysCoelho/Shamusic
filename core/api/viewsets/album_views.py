from rest_framework import viewsets

from core.api.serializers import AlbumListStringRelatedFieldSerializer
from core.models import Album


class AlbumListRetrieve(viewsets.ReadOnlyModelViewSet):
    queryset = Album.objects.all().select_related("band")
    serializer_class = AlbumListStringRelatedFieldSerializer
