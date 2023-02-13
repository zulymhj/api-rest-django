import logging
from rest_framework import serializers
from shop.models import Order, OrderItem, Customer, Cart
from shop.serializers.input import OrderItemInputSerializer, CustomerInputSerializer

logger = logging.getLogger(__name__)


class OrderInputSerializer(serializers.ModelSerializer):
    cart = serializers.PrimaryKeyRelatedField(
        many=False,
        allow_null=True,
        queryset=Cart.objects.all().filter(status=0),
        help_text="ID cart"
    )
    customer = CustomerInputSerializer()
    items = OrderItemInputSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'cart',
            'customer',
            'items'
        )

    def create(self, validated_data):
        # save customer
        customer_data = validated_data.pop('customer')
        customer = Customer.objects.all().filter(email=customer_data['email']).first()
        if customer is None:
            customer = Customer.objects.create(**customer_data)
        else:
            customer.address = customer_data['address']
            customer.save()
        validated_data['customer'] = customer
        # save items
        items = validated_data.pop('items')
        instance = Order.objects.create(**validated_data)
        total = 0
        for item in items:
            item['order'] = instance
            product = item['product']
            # only save when product not is deleted
            if product.status == 1:
                subtotal = round((product.price_unit * item['quantity']), 2)
                total = total + subtotal
                OrderItem.objects.create(**item)
        instance.total = total
        instance.save()
        return instance

    def update(self, instance, validated_data):
        # save customer
        customer_data = validated_data.pop('customer')
        customer = Customer.objects.all().filter(email=customer_data['email']).first()
        if customer is None:
            customer = Customer.objects.create(**customer_data)
        else:
            customer.address = customer_data['address']
            customer.save()
        validated_data['customer'] = customer

        # save items
        delete_items = OrderItem.objects.all().filter(order__id=instance.id).delete()
        items = validated_data.pop('items')
        total = 0
        for item in items:
            item['order'] = instance
            product = item['product']
            subtotal = round((product.price_unit * item['quantity']), 2)
            total = total + subtotal
            OrderItem.objects.create(**item)
        instance.total = total
        instance.save()
        return instance
