import logging
from rest_framework import serializers
from shop.models import OrderItem
from shop.serializers.output import ProductOutputSerializer

logger = logging.getLogger(__name__)


class OrderItemOutputSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = (
            'product',
            'quantity',
            'price'
        )

    @staticmethod
    def get_product(obj):
        product = ProductOutputSerializer(obj.product).data
        return product

    @staticmethod
    def get_price(obj):
        price = round((obj.product.price_unit * obj.quantity), 2)
        return price
