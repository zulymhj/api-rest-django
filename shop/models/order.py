from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models.customer import Customer
from shop.models.cart import Cart
from catalog.models.product import Product
from shop import STATUS_ORDER
from django.db.models.signals import post_save
from shop.signals import update_status_cart


class Order(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        verbose_name=_("Customer"),
        related_name="order_customer",
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.PROTECT,
        verbose_name=_("Cart"),
        related_name="order_cart",
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
                                   through='OrderItem',
                                   related_name='order_items')
    status = models.SmallIntegerField(
        _("status"),
        choices=STATUS_ORDER,
        blank=True,
        null=True,
        default=1,
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
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")


post_save.connect(update_status_cart, sender=Order)
