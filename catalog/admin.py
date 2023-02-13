from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from catalog.models import Product, Category, Brand, Color


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code',
                    'get_category', 'get_color_primary',
                    'get_brand', 'stock_initial',
                    'stock_now', 'image',
                    'status', 'created_at',
                    'updated_at', 'deleted_at']
    ordering = ("id",)
    list_filter = ("category__name","name")

    def get_category(self, obj):
        return obj.category.name

    get_category.short_description = "Category"
    get_category.empty_value_display = 'Not category selected'

    def get_color_primary(self, obj):
        return obj.color_primary.name

    get_color_primary.short_description = "Color"
    get_color_primary.empty_value_display = 'Not color primary selected'

    def get_brand(self, obj):
        return obj.brand.name

    get_brand.short_description = "Brand"
    get_brand.empty_value_display = 'Not brand selected'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        f.name for f in Category._meta.fields if f.name not in [
            "id",
        ]
    ]


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = [
        f.name for f in Color._meta.fields if f.name not in [
            "id",
        ]
    ]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [
        f.name for f in Brand._meta.fields if f.name not in [
            "id",
        ]
    ]
