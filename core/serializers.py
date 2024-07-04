from rest_framework import serializers

from .models import Album, Band


class BandNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ("name",)


class AlbumSerializer(serializers.ModelSerializer):
    band = BandNestedSerializer()

    class Meta:
        model = Album
        fields = [
            "id",
            "title",
            "release_date",
            "band",
            "cover",
        ]
        # depth = 1


class AlbumListStringRelatedFieldSerializer(serializers.ModelSerializer):
    band = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Album
        fields = [
            "id",
            "title",
            "release_date",
            "band",
            "cover",
        ]
        read_only_fields = [
            "band",
        ]


class AlbumCreateSerializer(serializers.ModelSerializer):
    band = serializers.PrimaryKeyRelatedField(queryset=Band.objects.all())

    class Meta:
        model = Album
        fields = [
            "id",
            "title",
            "release_date",
            "band",
            "cover",
        ]


class BandSerializer(serializers.ModelSerializer):
    genre = serializers.SerializerMethodField()

    class Meta:
        model = Band
        fields = "__all__"

    def get_genre(self, instance):
        return instance.get_genre_display()
