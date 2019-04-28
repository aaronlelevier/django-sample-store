from model_mommy import mommy
from rest_framework.test import APITestCase

from product.models import Product


class ProductViewTests(APITestCase):
    def test_list(self):
        product = mommy.make(Product)

        ret = self.client.get('/api/products/')

        assert ret.status_code == 200, ret.content
        data = ret.json()
        assert data['count'] == 1
        assert data['results'][0]['id'] == product.id
        assert 'name' in data['results'][0]
        assert 'price' in data['results'][0]
