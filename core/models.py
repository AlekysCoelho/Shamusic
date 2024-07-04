import datetime
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from .validators import validate_image_extension_and_mime_type


def upload_image(instancia, filename) -> str:
    """Define image name."""
    return f"{instancia.id}-{filename}"


class Band(models.Model):
    """Defines the band model."""

    class Genre(models.TextChoices):
        """Musical genres"""

        HEAVY_METAL = "HM", ("Heavy Metal")
        THRASH_METAL = "TM", ("Thrash Metal")
        HARD_ROCK = "HR", ("Hard Rock")
        POWER_METAL = "PM", ("Power Metal")
        DEATH_METAL = "DM", ("Death Metal")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Band name"), max_length=30)
    genre = models.CharField(
        _("Band genre"), max_length=2, choices=Genre.choices, default=Genre.HEAVY_METAL
    )
    bio = models.TextField(_("Band biography"), blank=True, null=True, editable=True)
    cover = models.ImageField(
        _("Cover image"),
        upload_to=f"band/{upload_image}",
        validators=[validate_image_extension_and_mime_type],
        blank=True,
        null=True,
    )
    created_at = models.DateField(_("Year the band was founded"), blank=True, null=True)

    class Meta:
        db_table = "Bands"
        ordering = ["genre", "name"]
        verbose_name_plural = "Bands"

    def __str__(self) -> str:
        return f"{self.name}"


class Album(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_("Album name"), max_length=50)
    release_date = models.DateField(
        _("Release date"), max_length=30, blank=True, null=True
    )
    band = models.ForeignKey(
        Band,
        on_delete=models.CASCADE,
        related_name="albums",
        related_query_name="album",
    )
    cover = models.ImageField(
        _("Cover image"),
        upload_to=f"album/{upload_image}",
        validators=[validate_image_extension_and_mime_type],
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["band", "title"]

    def __str__(self) -> str:
        return f"{self.title}"

    @property
    def get_amount_tracks(self) -> int:
        """Calculates the number of songs in the album"""
        return self.tracks.count()
