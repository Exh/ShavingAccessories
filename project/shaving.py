
class User(object):
	def __init__(self, subscribing = None):
		self._subscribing = subscribing

	@property
	def subscribing(self):
		return self._subscribing

	@subscribing.setter
	def subscribing(self, v):
		self._subscribing = v


class Subscribing(object):
	def __init__(self, product = None):
		self._product = product

	@property
	def product(self):
		return self._product

	@product.setter
	def product(self, v):
		self._product = v


class Product(object):
	def __init__(self, title, price):
		self._title = title
		self._price = price

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, v):
		self._title = v


	@property
	def price(self):
		return self._price

	@price.setter
	def price(self, v):
		self._price = v

class ProductBuilder(object):
	def __init__(self):
		self._title = ""
		self._price = 0

	def create(self):
		return Product(self._title, self._price)

	def withTitle(self, title):
		self._title = age
		return self

	def withPrice(self, price):
		self._price = price
		return self
