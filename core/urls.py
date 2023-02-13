"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import (
    include,
    path,
    re_path,
    reverse_lazy
)
from .schema import schema_view
from django.views.generic.base import RedirectView


ADMIN_URLS = [
    path("", RedirectView.as_view(url=reverse_lazy("admin:index")), name="home"),
    path('admin/', admin.site.urls),
]
API_URLS = [
    # API base url
    re_path(r"^api/v1/",
            include(
                [
                    re_path(r"^catalog/", include("catalog.urls", namespace="catalog")),
                    re_path(r"^shop/", include("shop.urls", namespace="shop")),

# Swagger & Redoc
                re_path(
                    r"^swagger(?P<format>\.json|\.yaml)$",
                    schema_view.without_ui(cache_timeout=0),
                    name="schema-json",
                ),
                re_path(
                    r"^swagger/$",
                    schema_view.with_ui("swagger", cache_timeout=0),
                    name="schema-swagger-ui",
                ),
                re_path(
                    r"^redoc/$",
                    schema_view.with_ui("redoc", cache_timeout=0),
                    name="schema-redoc",
                ),
                re_path(
                    r"^docs/$",
                    schema_view.with_ui("swagger", cache_timeout=0),
                    name="schema-swagger-ui",
                ),
                ]
            )
            )
]
THIRD_PARTY_URLS = [
    # Django AllAuth
    re_path(r"^accounts/", include("allauth.urls")),
]

urlpatterns = ADMIN_URLS + API_URLS + THIRD_PARTY_URLS
