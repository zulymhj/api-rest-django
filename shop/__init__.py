from django.utils.translation import gettext_lazy as _

STATUS_CUSTOMER = (
    (0, _("Innactive")),
    (1, _("Active")),
)

STATUS_CART = (
    (0, _("Pending")),
    (1, _("Bought")),
    (2, _("Cancelled")),
)

STATUS_ORDER = (
    (0, _("inactive")),
    (1, _("Open")),
    (2, _("Cancelled")),
    (3, _("Paid")),
    (4, _("Payment declined")),
    (5, _("Deliveried")),
)
