import logging
from rest_framework import serializers
from catalog.models import Product, Color, Brand, Category

logger = logging.getLogger(__name__)


class ProductInputSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        many=False,
        write_only=True,
        allow_null=False,
        queryset=Category.objects.all(),
        help_text="category ID"
    )
    brand = serializers.PrimaryKeyRelatedField(
        many=False,
        write_only=True,
        allow_null=False,
        queryset=Brand.objects.all(),
        help_text="brand ID"
    )
    color_brand = serializers.PrimaryKeyRelatedField(
        many=False,
        allow_null=True,
        queryset=Color.objects.all(),
        help_text="ID color brand"
    )
    color_primary = serializers.PrimaryKeyRelatedField(
        many=False,
        allow_null=True,
        queryset=Color.objects.all(),
        help_text="ID color primary"
    )
    color_secondary = serializers.PrimaryKeyRelatedField(
        many=False,
        allow_null=True,
        queryset=Color.objects.all(),
        help_text="ID color secondary"
    )
    image = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'code',
            'price_unit',
            'stock_initial',
            'status',
            'category',
            'brand',
            'color_brand',
            'color_primary',
            'color_secondary',
            'type',
            'size',
            'has_sleeves',
            'image'
        )
