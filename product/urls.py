from django.urls import path, include
from rest_framework import routers
from debug_toolbar.toolbar import debug_toolbar_urls

from product import viewsets

router = routers.SimpleRouter()
router.register(r"product", viewsets.ProductViewSet, basename="product")
router.register(r"category", viewsets.CategoryViewSet, basename="category")

urlpatterns = [path("", include(router.urls))] + debug_toolbar_urls()
