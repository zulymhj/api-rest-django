from django.urls import path, include
from rest_framework import routers
from django.conf import settings

from catalog.views import (
    ProductView
)

if settings.DEBUG:
    router = routers.DefaultRouter()
else:
    router = routers.SimpleRouter()
router.register("product", ProductView,
                basename='product')

app_name = "catalog"
urlpatterns = [
    path('', include(router.urls)),
]
