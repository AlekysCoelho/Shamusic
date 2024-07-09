from django_filters import rest_framework as filters

from core.models import Track


class TrackFilter(filters.FilterSet):
    band = filters.CharFilter(field_name="album__band__name", lookup_expr="icontains")
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
    album = filters.CharFilter(field_name="album__title", lookup_expr="icontains")
    single = filters.BooleanFilter()

    class Meta:
        model = Track
        fields = (
            "title",
            "single",
            "album",
            "band",
        )
