from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [AllowAny]
