from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from product.models import Category
from product.serializers.category_serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AllowAny]
