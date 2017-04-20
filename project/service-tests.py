import unittest
from shaving import User
from shaving import Subscribing

class ShavingServiceTests(unittest.TestCase):
	def test_user_can_setup_Shave_as_product_of_subscribing(self):
		user = User()
		subscribing = Subscribing()
		product = Product()

		subscribing.product(product)
		user.subscribing(subscribing)


		self.assertEqual(user.subscribing.product.title, "Shave")

if __name__ == '__main__':
	unittest.main()
