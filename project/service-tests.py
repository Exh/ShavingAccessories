import unittest
from shaving import User
from shaving import Subscribing
from shaving import Product

class ShavingServiceTests(unittest.TestCase):
	def test_user_can_setup_Shave_as_product_of_subscribing(self):
		product = Product()
		subscribing = Subscribing(product)
		user = User(subscribing)

		self.assertEqual(user.subscribing.product.title, "Shave")

if __name__ == '__main__':
	unittest.main()
