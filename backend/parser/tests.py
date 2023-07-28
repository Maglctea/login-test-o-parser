from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from parser.models import Product


class ParserApiTestCase(APITestCase):

    def test_get_products(self):
        url = reverse('products')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_post_products_success(self):
        url = reverse('products')
        response = self.client.post(url, data={'products_count': 20})
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_post_products_fail(self):
        url = reverse('products')
        response = self.client.post(url, data={'products_count': 51})
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_get_product(self):
        url = reverse('detail_product', args=[1000])
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
