from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    first_name = models.CharField(
        _("First name"),
        max_length=250
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class ExtendedUserBase(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name=_("User"),
        related_name="%(app_label)s_%(class)s_related_user",
    )

    class Meta:
        abstract = True
