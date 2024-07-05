from rest_framework import serializers

from core.models import Album, Band, Musician, Track

# NESTED


class BandNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ("name",)


# ALBUM
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


# BAND
class BandSerializer(serializers.ModelSerializer):
    genre = serializers.SerializerMethodField()

    class Meta:
        model = Band
        fields = "__all__"

    def get_genre(self, instance):
        return instance.get_genre_display()


# MUSICIAN
class MusicianSerializer(serializers.ModelSerializer):
    type_musician = serializers.SerializerMethodField()
    band = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Musician
        fields = "__all__"
        read_only_fields = [
            "band",
        ]

    def get_type_musician(self, instancia):
        return instancia.get_type_musician_display()


# TRACK


class TrackSerializer(serializers.ModelSerializer):
    by_composers = serializers.StringRelatedField(read_only=True, many=True)
    album = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Track
        fields = [
            "id",
            "title",
            "track_number",
            "duration",
            "album",
            "by_composers",
            "single",
        ]
