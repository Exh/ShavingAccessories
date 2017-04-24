import unittest
from shaving import User
from shaving import Subscribing
from shaving import Product
from shaving import ProductBuilder
from shaving import OnceTwoMonth
from datetime import date


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

		self.assertEqual(subscribing.isActive, False)

	def test_user_can_setup_shave_as_product_once_a_month_as_shipping_interval_start_date_14_jan_2017_to_14_jan_2017_spend_money_is_1(self):
		product = ProductBuilder().withTitle("Shave").withPrice(1).create()
		subscribing = Subscribing(product, OnceTwoMonth(14))
		subscribing.startDate = date(2017, 1, 14)
		user = User(subscribing)
		user.updateCurrentDate(date(2017, 1, 14))

		self.assertEqual(user.spendCash, 1)

	def test_user_can_setup_shave_and_gel_as_product_once_a_month_as_shipping_interval_start_date_14_jan_2017_to_14_jan_2017_spend_money_is_9(self):
		product = ProductBuilder().withTitle("Shave + Gel").withPrice(9).create()
		subscribing = Subscribing(product, OnceTwoMonth(14))
		subscribing.startDate = date(2017, 1, 14)
		user = User(subscribing, date(2017, 1, 10))
		user.updateCurrentDate(date(2017, 1, 14))

		self.assertEqual(user.spendCash, 9)


if __name__ == '__main__':
	unittest.main()
