import json

import pytest

pytestmark = pytest.mark.django_db


class TestBrandEndpoint:
    endpoint = '/api/brand/'

    def test_brand_get(self, brand_factory, api_client):
        # Arrange
        brand_factory.create_batch(4)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4
