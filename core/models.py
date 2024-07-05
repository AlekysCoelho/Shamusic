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


class Musician(models.Model):
    class TypeMusician(models.TextChoices):
        VOCAL = "V", _("Vocal")
        GUITAR = "G", _("Guitar")
        BASS = "B", _("Bass")
        DRUMMER = "D", _("Drummer")
        VOCAL_GUITAR = "VG", _("Vocal and Guitar")
        VOCAL_BASS = "VB", _("Vocal and Bass")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(_("First name"), max_length=30)
    last_name = models.CharField(_("Last name"), max_length=30)
    date_birth = models.DateField(
        _("Date of birth"),
        help_text=f"Exemplo: (2024-05-30)",
        blank=True,
        null=True,
    )
    type_musician = models.CharField(
        _("Type of musician / Instrument"),
        max_length=2,
        choices=TypeMusician.choices,
        blank=True,
        null=True,
    )
    band = models.ForeignKey(
        Band,
        on_delete=models.PROTECT,
        related_name="musicians",
        related_query_name="musician",
        blank=True,
        null=True,
    )
    cover = models.ImageField(
        _("Cover image"),
        upload_to=f"musician/{upload_image}",
        validators=[validate_image_extension_and_mime_type],
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["band", "last_name"]

    def __str__(self) -> str:
        return f"{self.last_name}"

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def get_age(self) -> str:
        """Tell the musician's age"""
        today = datetime.date.today()

        try:
            birthday = self.date_birth.replace(year=today.year)

        except ValueError:
            birthday = self.date_birth.replace(
                year=today.year, month=today.month + 1, day=1
            )
        if birthday > today:
            return f"{today.year - self.date_birth.year - 1} years"
        else:
            return f"{today.year - self.date_birth.year} years"


class Track(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_("Track"), max_length=100)
    track_number = models.PositiveSmallIntegerField(
        _("track number in the song list"), blank=True, null=True
    )
    by_composers = models.ManyToManyField(
        Musician,
        related_name="tracks",
        related_query_name="track",
        blank=True,
    )
    duration = models.CharField(_("Song length"), max_length=5, blank=True, null=True)
    album = models.ForeignKey(
        Album,
        on_delete=models.PROTECT,
        related_name="tracks",
        related_query_name="track",
        blank=True,
        null=True,
    )
    letter = models.TextField(_("Letter"), blank=True, null=True, editable=True)
    single = models.BooleanField(_("Single"), default=False)
    title_track = models.BooleanField(_("Song title track"), default=False)
    release_date = models.DateField(
        _("Release date"), max_length=30, blank=True, null=True
    )

    class Meta:
        ordering = ["album", "title"]

    def __str__(self) -> str:
        composers = []
        if self.by_composers.count() > 1:
            for composer in self.by_composers.values_list("last_name"):
                composers.append(composer[0])
            return f"{self.title} by: {composers}"
        return f"{self.title} by: "
