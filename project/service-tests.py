import unittest
from shaving import User
from shaving import Subscribing
from shaving import Product
from shaving import ProductBuilder
from shaving import OnceTwoMonth

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

	def test_user_can_setup_once_two_month_as_shipping_interval_of_subscribing(self):
		product = ProductBuilder().withTitle("Shave + Gel + Aftershaves").create()
		subscribing = Subscribing(product, OnceTwoMonth(1))
		user = User(subscribing)

		self.assertEqual(user.subscribing.interval.title, "Once Two Month")

	def test_user_can_deactivate_subscribing(self):
		product = ProductBuilder().withTitle("Shave + Gel + Aftershaves").create()
		subscribing = Subscribing(product, OnceTwoMonth(1))
		user = User(subscribing)

		self.assertEqual(subscribing.isActive(), False)



if __name__ == '__main__':
	unittest.main()
