from django.db import models
from django.utils.translation import gettext_lazy as _
from catalog.models.product import Product

from django.db.models.signals import post_save, post_delete
from shop.signals import update_stock_now_product, restore_stock_now_product


class OrderItem(models.Model):
    order = models.ForeignKey(
        "Order",
        on_delete=models.CASCADE,
        related_name="order",
        verbose_name=_("order"),
        null=False,
        blank=False,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="order_item_product",
        verbose_name=_("product"),
        null=False,
        blank=False,
    )
    quantity = models.IntegerField(
        _("Count of products"),
        default=0,
        blank=False,
        null=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        editable=True,
    )

    class Meta:
        verbose_name = _("Order item")
        verbose_name_plural = _("Order items")


post_save.connect(update_stock_now_product, sender=OrderItem)
post_delete.connect(restore_stock_now_product, sender=OrderItem)
