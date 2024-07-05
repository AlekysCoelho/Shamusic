from rest_framework import viewsets

from core.api.serializers import MusicianSerializer
from core.models import Musician


class MusiciansViewsets(viewsets.ModelViewSet):

    queryset = Musician.objects.all().select_related("band")
    serializer_class = MusicianSerializer


class MusiciansListRetrieve(viewsets.ReadOnlyModelViewSet):
    queryset = Musician.objects.all().select_related("band")
    serializer_class = MusicianSerializer
