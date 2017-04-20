import unittest
from shaving import User
from shaving import Subscribing
from shaving import Product
from shaving import ProductBuilder

class ShavingServiceTests(unittest.TestCase):
	def test_user_can_setup_Shave_as_product_of_subscribing(self):
		product = ProductBuilder().withTitle("Shave").create()
		subscribing = Subscribing(product)
		user = User(subscribing)

		self.assertEqual(user.subscribing.product.title, "Shave")

	def test_user_can_setup_Shave_and_Gel_as_product_of_subscribing(self):
		product = ProductBuilder().withTitle("Shave + Gel").create()
		subscribing = Subscribing(product)
		user = User(subscribing)

		self.assertEqual(user.subscribing.product.title, "Shave + Gel")

	def test_user_can_setup_Shave_and_Gel_and_Aftershaves_as_product_of_subscribing(self):
		product = ProductBuilder().withTitle("Shave + Gel + Aftershaves").create()
		subscribing = Subscribing(product)
		user = User(subscribing)

		self.assertEqual(user.subscribing.product.title, "Shave + Gel + Aftershaves")

if __name__ == '__main__':
	unittest.main()
