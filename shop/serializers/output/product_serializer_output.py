import logging
from rest_framework import serializers
from catalog.models import Product
from catalog import STATUS_PRODUCT

logger = logging.getLogger(__name__)


class ProductOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price_unit',
            'image',
            'status'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['status'] = STATUS_PRODUCT[data['status']][1]
        return data
