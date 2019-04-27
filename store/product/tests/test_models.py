import unittest
from product import models as product_models

from model_mommy import mommy


class ProductTests(unittest.TestCase):

    def test_save__sets_in_stock_based_on_quantity(self):
        product = mommy.make('Product', quantity=1)

        assert product.in_stock

        product2 = mommy.make('Product', quantity=0)

        assert not product2.in_stock
