from django.db import models
from django.utils.translation import gettext_lazy as _
from catalog.models.product import Product


class CartItem(models.Model):
    cart = models.ForeignKey(
        "Cart",
        on_delete=models.CASCADE,
        related_name="cart",
        verbose_name=_("Cart"),
        null=False,
        blank=False,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product",
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
        verbose_name = _("Cart item")
        verbose_name_plural = _("Cart items")
