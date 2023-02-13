import logging
from catalog.models.product import Product
from shop.models import Cart

logger = logging.getLogger(__name__)


def update_stock_now_product(sender, instance, created, **kwargs):
    if created is True:
        try:
            product = Product.objects.all().filter(id=instance.product.id).first()
            product.stock_now = product.stock_initial - instance.quantity
            product.save()
        except Exception as ex:
            logger.info("update_stock_now_product - Signals")
            logger.error(ex)


def restore_stock_now_product(sender, instance, *args, **kwargs):
    try:
        product = Product.objects.all().filter(id=instance.product.id).first()
        product.stock_now = product.stock_now + instance.quantity
        product.save()
    except Exception as ex:
        logger.info("restore_stock_now_product - Signals")
        logger.error(ex)


def update_status_cart(sender, instance, created, **kwargs):
    try:
        cart = Cart.objects.all().filter(status=0).first()
        cart.customer = instance.customer
        cart.status = 1
        cart.save()
    except Exception as ex:
        logger.info("update_status_cart - Signals")
        logger.error(ex)
