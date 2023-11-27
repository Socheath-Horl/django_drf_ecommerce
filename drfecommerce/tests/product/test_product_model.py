import pytest

pytestmark = pytest.mark.django_db


class TestProductModel:
    def test_str_method(self, product_factory):
        # Arrage
        # Act
        x = product_factory(name="test_product")
        # Assert
        assert x.__str__() == "test_product"
