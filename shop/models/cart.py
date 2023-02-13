from django.db import models
from django.utils.translation import gettext_lazy as _
from catalog.models.product import Product
from shop.models import Customer
from shop import STATUS_CART


class Cart(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        verbose_name=_("Customer"),
        related_name="cart_customer",
        blank=True,
        null=True,
    )
    total = models.DecimalField(
        _("Total"),
        max_digits=5,
        decimal_places=2,
        default=0
    )
    items = models.ManyToManyField(Product,
                                   through='CartItem',
                                   related_name='cart_items')
    status = models.SmallIntegerField(
        _("status"),
        choices=STATUS_CART,
        blank=True,
        null=True,
        default=0,
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
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")
