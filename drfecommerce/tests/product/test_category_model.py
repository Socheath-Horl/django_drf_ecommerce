import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Arrage
        # Act
        x = category_factory(name="test_cat")
        # Assert
        assert x.__str__() == "test_cat"
