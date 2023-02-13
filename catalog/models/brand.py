from django.db import models
from django.utils.translation import gettext_lazy as _


class Brand(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=250
    )
    logo = models.FileField(
        _("Logo"),
        blank=True,
        null=True,
        upload_to="brand/logo",
    )

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return f"{self.name}"
