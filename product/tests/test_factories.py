import pytest
from product.factories import CategoryFactory


class TestCategoryFactory:
    def test_create_category(self):
        category = CategoryFactory.create()

        assert category is not None
        assert category.title is not None
        assert category.slug is not None
        assert category.description is not None
        assert category.active in [True, False]
