from rest_framework import serializers

from order.models.order import Order
from product.models import Product
from product.serializers.product_serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True, many=True, source="product"
    )
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total

    class Meta:
        model = Order
        fields = ["id", "user", "product", "product_id", "total"]
        extra_kwargs = {"product": {"required": False}}

    def create(self, validated_data):
        product_data = validated_data.pop("product")
        user_data = validated_data.pop("user")

        order = Order.objects.create(user=user_data)
        for product in product_data:
            order.product.add(product)
        return order
