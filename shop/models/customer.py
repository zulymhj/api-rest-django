from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models.user import User
from shop import STATUS_CUSTOMER


class Customer(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name=_("User"),
        related_name="customer_user",
        blank=True,
        null=True
    )
    first_name = models.CharField(
        _("First name"),
        max_length=250
    )
    surname = models.CharField(
        _("Surname"),
        max_length=250
    )
    email = models.CharField(
        _("Email"),
        max_length=250
    )
    cellphone = models.CharField(
        _("Cellphone"),
        max_length=250
    )
    address = models.CharField(
        _("Address"),
        max_length=250
    )
    status = models.SmallIntegerField(
        _("status"),
        choices=STATUS_CUSTOMER,
        blank=True,
        null=True,
        default=1
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
    deleted_at = models.DateTimeField(
        auto_now=False,
        null=True,
        blank=True,
        editable=False,
    )

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return f"{self.first_name}"
