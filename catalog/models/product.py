from django.db import models
from django.utils.translation import gettext_lazy as _
from catalog.models import (Color, Brand, Category)
from catalog import STATUS_PRODUCT, SIZE_PRODUCT, TYPE_PRODUCT
from core.models.user import User


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="product_category",
        verbose_name=_("Category"),
        help_text=_("Selected if is T-shirt o cap")
    )
    name = models.CharField(
        _("Name"),
        max_length=250,
        null=False,
        blank=False,
    )
    description = models.CharField(
        _("Description"),
        max_length=500,
        null=False,
        blank=False,
    )
    code = models.CharField(
        _("Code"),
        max_length=20
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name="product_brand",
        verbose_name=_("brand"),
        null=False,
        blank=False,
    )
    color_brand = models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        related_name="product_color_brand",
        verbose_name=_("Color brand"),
        null=True,
        blank=True,
    )
    color_primary = models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        related_name="product_color_primary",
        verbose_name=_("Primary color"),
        null=False,
        blank=False,
    )
    color_secondary = models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        related_name="product_color_secondary",
        verbose_name=_("secondary color"),
        null=False,
        blank=False,
    )
    price_unit = models.DecimalField(
        _("Price unitity"),
        max_digits=5,
        decimal_places=2
    )
    material = models.CharField(
        _("Material"),
        max_length=250,
        null=True,
        blank=True,
    )
    type = models.SmallIntegerField(
        _("Type"),
        choices=TYPE_PRODUCT,
        blank=True,
        null=True,
        default=0
    )
    size = models.CharField(
        _("Size"),
        choices=SIZE_PRODUCT,
        blank=True,
        null=True,
        max_length=4
    )
    has_sleeves = models.BooleanField(
        _("has_sleeves"),
        blank=True,
        null=True,
    )

    stock_initial = models.IntegerField(
        _("Stock initial"),
        default=0,
        blank=False,
        null=False
    )
    stock_now = models.IntegerField(
        _("Stock now"),
        default=0,
        blank=True,
        null=True
    )
    image = models.FileField(
        _("Image"),
        blank=True,
        null=True,
        upload_to="product/image",
    )
    status = models.SmallIntegerField(
        _("status"),
        choices=STATUS_PRODUCT,
        blank=True,
        null=True,
        default=0
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_("created by"),
        related_name="%(app_label)s_%(class)s_related_created_by",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        editable=False,
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        verbose_name=_("updated by"),
        related_name="%(app_label)s_%(class)s_related_updated_by",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
        editable=True,
    )
    deleted_at = models.DateTimeField(
        auto_now=False,
        null=True,
        blank=True,
        editable=False,
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return f"{self.name}"
