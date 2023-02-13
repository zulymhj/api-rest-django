import logging
from rest_framework import serializers
from shop.models import Order, OrderItem
from catalog.models.product import Product

logger = logging.getLogger(__name__)


class OrderItemInputSerializer(serializers.ModelSerializer):
    # order = serializers.PrimaryKeyRelatedField(
    #     many=False,
    #     allow_null=False,
    #     queryset=Order.objects.all(),
    #     help_text="ID cart"
    # )
    product = serializers.PrimaryKeyRelatedField(
        many=False,
        allow_null=False,
        queryset=Product.objects.all(),
        help_text="ID product"
    )

    # product = serializers.IntegerField(),

    class Meta:
        model = OrderItem
        fields = (
            'product',
            'quantity'
        )
