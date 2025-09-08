import pytest
from order.serializers import OrderSerializer
from order.factories import OrderFactory
from product.factories import ProductFactory


class TestOrderSerializer:

    def test_order_serialization(self):

        products = ProductFactory.create_batch(2, price=100)
        order = OrderFactory()
        order.product.set(products)

        serializer = OrderSerializer(order)
        data = serializer.data

        assert "product" in data
        assert "total" in data
        assert data["total"] == 200

    def test_order_total_calculation(self):
   
        products = ProductFactory.create_batch(3, price=50)
        order = OrderFactory()
        order.product.set(products)

        serializer = OrderSerializer(order)
        data = serializer.data

        assert data["total"] == 150

    def test_order_without_products(self):
        order = OrderFactory()

        serializer = OrderSerializer(order)
        data = serializer.data

        assert data["total"] == 0
