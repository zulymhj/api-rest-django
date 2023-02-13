from django.urls import path, include
from rest_framework import routers
from django.conf import settings

from shop.views import (
    CartView, OrderView
)

if settings.DEBUG:
    router = routers.DefaultRouter()
else:
    router = routers.SimpleRouter()
router.register("cart", CartView,
                basename='cart')
router.register("order", OrderView,
                basename='order')

app_name = "shop"
urlpatterns = [
    path('', include(router.urls)),
]
