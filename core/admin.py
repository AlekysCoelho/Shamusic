from typing import Any

from django.contrib import admin
from django.db.models import Prefetch
from django.db.models.query import QuerySet
from django.http import HttpRequest

from core.models import Album, Band, Musician, Track


class TracksInline(admin.TabularInline):
    model = Track


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    model = Album
    list_display = [
        "title",
        "band",
        "release_date",
    ]
    inlines = [
        TracksInline,
    ]


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    model = Musician
    list_display = [
        "name",
        "genre",
    ]


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    model = Musician
    list_display = [
        "last_name",
        "type_musician",
        "date_birth",
        "band",
    ]


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    # model = Track
    list_display = [
        "title",
        "duration",
        "by_members",
    ]

    def by_members(self, obj):
        return ", ".join(
            [member.last_name for member in obj.by_composers.prefetch_related("tracks")]
        )
