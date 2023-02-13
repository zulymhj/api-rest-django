import logging
from rest_framework import serializers
from shop.models import Order, OrderItem
from shop.serializers.output import OrderItemOutputSerializer, CustomerOutputSerializer

logger = logging.getLogger(__name__)


class OrderOutputSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'id',
            'total',
            'customer',
            'items',
            'updated_at',
        )

    @staticmethod
    def get_items(obj):
        items = OrderItem.objects.filter(order__id=obj.id)
        order_items = OrderItemOutputSerializer(items, many=True).data
        return order_items

    @staticmethod
    def get_customer(obj):
        customer = CustomerOutputSerializer(obj.customer).data
        return customer
