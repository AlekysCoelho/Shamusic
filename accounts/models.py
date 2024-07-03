from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Users(AbstractUser):
    bio = models.TextField(_("Biography"), blank=True, null=True)
