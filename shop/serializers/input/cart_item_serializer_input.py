import logging
from rest_framework import serializers
from shop.models import Cart, CartItem
from catalog.models.product import Product

logger = logging.getLogger(__name__)


class CartItemInputSerializer(serializers.ModelSerializer):
    product = serializers.IntegerField(),

    class Meta:
        model = CartItem
        fields = (
            'product',
            'quantity'
        )
