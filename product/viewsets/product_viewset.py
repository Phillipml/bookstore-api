from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from product.models import Product
from product.serializers.product_serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Product.objects.all()
