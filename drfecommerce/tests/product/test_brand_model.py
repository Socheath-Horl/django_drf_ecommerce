import pytest

pytestmark = pytest.mark.django_db


class TestBrandModel:
    def test_str_method(self, brand_factory):
        # Arrage
        # Act
        x = brand_factory(name="test_brand")
        # Assert
        assert x.__str__() == "test_brand"
