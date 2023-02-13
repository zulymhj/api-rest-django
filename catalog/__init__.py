from django.utils.translation import gettext_lazy as _

STATUS_PRODUCT = (
    (0, _("Innactive")),
    (1, _("Active")),
    (2, _("Deleted")),
)

PRODUCT_COLOR_ORDER = (
    (1, _("Principal")),
    (2, _("Secondary")),
)

SIZE_PRODUCT = (
    ('XS', _("XS")),
    ('S', _("S")),
    ('M', _("M")),
    ('L', _("L")),
)

TYPE_PRODUCT = (
    (1, _("Hombre")),
    (2, _("Mujer")),
    (3, _("Unisex")),
)