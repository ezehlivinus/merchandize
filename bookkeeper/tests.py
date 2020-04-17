from django.test import TestCase

from rest_framework.test import APIClient, APITestCase

from bookkeeper.api_views import *


class TestBrand(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.view = BrandViewSet.as_view({'get': 'list'})
        self.url = '/api/v1/brands'

    def test_create(self):
        params = {
            "name": "Itel3"
        }
        response = self.client.post(self.url, params)
        self.assertEqual(
            response.status_code, 201,
            f'Expected response code to be 201, received {response.status_code}'
        )

    def test_brand_list(self):
        response = self.client.get(self.url)
        self.assertEqual(
            response.status_code, 200,
            f'Expected response code to be 200, received {response.status_code}'
        )
