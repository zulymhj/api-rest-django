from django.db import models
from django.utils.translation import gettext_lazy as _


class Color(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=250
    )
    code = models.CharField(
        _("Code color"),
        max_length=250
    )

    class Meta:
        verbose_name = _("Color")
        verbose_name_plural = _("Colors")

    def __str__(self):
        return f"{self.name}"
