import logging
from rest_framework import serializers
from catalog.models import Product
from core import settings
logger = logging.getLogger(__name__)


class ProductOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'pk',
            'name',
            'description',
            'price_unit',
            'category',
            'brand',
            'image',
            'stock_now',
            'created_at'
        )


    def to_representation(self, instance):
        data = super().to_representation(instance)
        logo_default = str(settings.DOMAIN_NAME) + '/media/img-product-example.png'
        data['image'] = data['image'] if data['image'] else logo_default
        return data
