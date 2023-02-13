import logging
from rest_framework import serializers
from shop.models import Cart, CartItem
from catalog.models import Product
from shop.serializers.input import CartItemInputSerializer

logger = logging.getLogger(__name__)


class CartInputSerializer(serializers.ModelSerializer):
    items = CartItemInputSerializer(many=True)

    class Meta:
        model = Cart
        fields = (
            'id',
            'items',
        )

    @staticmethod
    def get_total(obj):
        total = 0
        items = CartItem.objects.filter(cart__id=obj.id)
        for item in items:
            product = Product.objects.get(id=item.product.id)
            subtotal = round((product.price_unit * item.quantity), 2)
            total = total + subtotal
        return total

    def create(self, validated_data):
        items = validated_data.pop('items')
        instance = Cart.objects.create(**validated_data)
        total = 0
        for item in items:
            product = item['product']
            subtotal = round((product.price_unit * item['quantity']), 2)
            total = total + subtotal
            item['cart'] = instance
            CartItem.objects.create(**item)
        instance.total = total
        instance.save()
        return instance

    def update(self, instance, validated_data):
        delete_items = CartItem.objects.all().filter(cart__id=instance.id).delete()
        items = validated_data.pop('items')
        total = 0
        for item in items:
            item['cart'] = instance
            product = item['product']
            subtotal = round((product.price_unit * item['quantity']), 2)
            total = total + subtotal
            CartItem.objects.create(**item)
        instance.total = total
        instance.save()
        return instance
