import logging
from rest_framework import serializers
from shop.models import Customer

logger = logging.getLogger(__name__)


class CustomerInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'first_name',
            'surname',
            'email',
            'address'
        )
