from datetime import date

class Interval():
	@property
	def days(self):
		return self._days


class OnceTwoMonth(Interval):
	def __init__(self, day):
		self._title = "Once Two Month"
		self._days = [day]

	@property
	def title(self):
		return self._title



class OnceAMonth(Interval):
	def __init__(self, day):
		self._title = "Once A Month"
		self._days = [day]

	@property
	def title(self):
		return self._title

class TwiceAMonth(Interval):
	def __init__(self, day1, day2):
		self._title = "Twice A Month"
		self._days = [day1, day2]

	@property
	def title(self):
		return self._title

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
	def __init__(self, product = None, interval = None):
		self._product = product
		self._interval = interval

	@property
	def product(self):
		return self._product

	@product.setter
	def product(self, v):
		self._product = v

	@property
	def interval(self):
		return self._interval

	@interval.setter
	def interval(self, v):
		self._interval = v


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
		self._title = title
		return self

	def withPrice(self, price):
		self._price = price
		return self
