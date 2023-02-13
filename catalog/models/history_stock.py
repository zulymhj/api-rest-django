from django.db import models
from django.utils.translation import gettext_lazy as _


class HistoryStock(models.Model):
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="history_stock_product",
        verbose_name=_("category"),
    )
    stock = models.IntegerField(
        _("Stock"),
        default=0,
        blank=True,
        null=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        editable=True,
    )

    class Meta:
        verbose_name = _("History Stock")
        verbose_name_plural = _("History Stock")
