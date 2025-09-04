from django.urls import path, include
from rest_framework import routers
from debug_toolbar.toolbar import debug_toolbar_urls

from order import viewsets

router = routers.SimpleRouter()
router.register(r"order", viewsets.OrderViewSet, basename="order")

urlpatterns = [path("", include(router.urls))] + debug_toolbar_urls()
