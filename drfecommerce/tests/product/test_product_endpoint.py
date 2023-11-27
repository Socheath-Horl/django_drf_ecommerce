import json

import pytest

pytestmark = pytest.mark.django_db


class TestProductEndpoint:
    endpoint = '/api/product/'

    def test_product_get(self, product_factory, api_client):
        # Arrange
        product_factory.create_batch(4)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4
