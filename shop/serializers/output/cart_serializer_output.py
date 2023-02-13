import logging
from rest_framework import serializers
from shop.models import Cart, CartItem
from shop.serializers.output import CartItemOutputSerializer

logger = logging.getLogger(__name__)


class CartOutputSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = (
            'id',
            'total',
            'items',
            'created_at',
            'updated_at'
        )

    @staticmethod
    def get_items(obj):
        items = CartItem.objects.filter(cart__id=obj.id)
        order_items = CartItemOutputSerializer(items, many=True).data
        return order_items
