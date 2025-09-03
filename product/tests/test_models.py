import pytest
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from product.models import Category, Product
from product.factories import CategoryFactory, ProductFactory


class TestCategoryModel:

    @pytest.mark.django_db
    def test_category_creation(self):
        category = CategoryFactory()
        assert category.title is not None
        assert category.slug is not None
        assert isinstance(category.active, bool)

    @pytest.mark.django_db
    def test_category_str_representation(self):
        category = CategoryFactory(title="terror")
        assert str(category) == "terror"

    @pytest.mark.django_db
    def test_category_slug_unique(self):
        CategoryFactory(slug="ficcao-category")
        with pytest.raises(IntegrityError):
            CategoryFactory(slug="ficcao-category")


class TestProductModel:
    @pytest.mark.django_db
    def test_product_creation(self):
        product = ProductFactory()
        assert product.title is not None
        assert product.price is not None
        assert product.active is True

    @pytest.mark.django_db
    def test_product_with_categories(self):

        categories = CategoryFactory.create_batch(3)
        product = ProductFactory()
        product.category.set(categories)
        assert product.category.count() == 3
