
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
