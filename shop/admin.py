from django.contrib import admin
from shop.models import Cart, Order, Customer, OrderItem, CartItem
from django.forms import ModelChoiceField, ModelForm


# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_customer', 'get_items', 'total', 'status', 'created_at', 'updated_at']
    ordering = ("updated_at",)
    list_filter = ("status",)
    readonly_fields = ('total', 'customer', 'get_items')

    def get_items(self, obj):
        items = CartItem.objects.filter(cart__id=obj.id)
        return len(items)

    get_items.short_description = "Items"
    get_items.empty_value_display = '0 items'

    def get_customer(self, obj):
        return obj.customer.first_name + ' ' + obj.customer.surname if obj.customer else 'Anonymous'

    get_customer.short_description = "Customer"
    get_customer.empty_value_display = 'Anonymous'


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['get_cart', 'get_product', 'quantity', 'updated_at']
    list_filter = ("cart__id", "updated_at")
    ordering = ("cart__id",)

    def get_cart(self, obj):
        return obj.cart.id

    get_cart.short_description = "ID cart"
    get_cart.empty_value_display = ''

    def get_product(self, obj):
        return obj.product.name if obj.product else ''

    get_product.short_description = "Product"
    get_product.empty_value_display = 'Product not available'


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        f.name for f in Customer._meta.fields if f.name not in [
            "id",
        ]
    ]
    list_filter = ("first_name", "status")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_cart', 'get_customer', 'get_items', 'total', 'status', 'created_at', 'updated_at']
    ordering = ("updated_at",)
    list_filter = ("status", "customer__first_name")
    readonly_fields = ('cart', 'total', 'customer', 'get_items')

    # forms = OrderAdminForm

    def get_cart(self, obj):
        return obj.cart.id if obj.cart else 0

    get_cart.short_description = "ID Cart"
    get_cart.empty_value_display = 'Not Cart'

    def get_customer(self, obj):
        return obj.customer.first_name + ' ' + obj.customer.surname if obj.customer else ''

    get_customer.short_description = "Customer"
    get_customer.empty_value_display = 'Not customer'

    def get_items(self, obj):
        items = OrderItem.objects.filter(order__id=obj.id)
        return len(items)

    get_items.short_description = "Items"
    get_items.empty_value_display = 'Not has items'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['get_order', 'get_product', 'quantity', 'updated_at']
    list_filter = ("order__id", "updated_at")
    ordering = ("order__id",)

    def get_order(self, obj):
        return obj.order.id

    get_order.short_description = "ID order"
    get_order.empty_value_display = ''

    def get_product(self, obj):
        return obj.product.name if obj.product else ''

    get_product.short_description = "Product"
    get_product.empty_value_display = 'Product not available'
