from datetime import date


class OnceTwoMonth:
	def __init__(self, day):
		self._title = "Once Two Month"
		self._days = [day]
		self._offset = 2

	@property
	def title(self):
		return self._title

	@property
	def days(self):
		return self._days


class OnceAMonth:
	def __init__(self, day):
		self._title = "Once A Month"
		self._days = [day]
		self._offset = 1

	@property
	def title(self):
		return self._title

	@property
	def days(self):
		return self._days


class TwiceAMonth:
	def __init__(self, day):
		self._title = "Twice A Month"
		self._days = [day, day + 15]
		self._offset = 0

	@property
	def title(self):
		return self._title

	@property
	def days(self):
		return self._days


class User(object):
	def __init__(self, subscribing=None, create_day=date.today()):
		self._subscribing = subscribing
		self._spendCash = 0
		self._currentDate = create_day

	@property
	def subscribing(self):
		return self._subscribing

	@subscribing.setter
	def subscribing(self, v):
		self._subscribing = v

	def updateCurrentDate(self, new_date):
		self._spendCash += self._subscribing.getCostForPeriod(self._currentDate, new_date)
		self._currentDate = new_date

	@property
	def spendCash(self):
		return self._spendCash


class Subscribing(object):
	def __init__(self, product = None, interval = None, d = None):
		self._product = product
		self._interval = interval
		self._active = False
		self._startDate = d

	@property
	def startDate(self):
		return self._startDate

	@startDate.setter
	def startDate(self, d):
		self._startDate = d

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

	@property
	def isActive(self):
		return self._active

	def getCostForPeriod(self, start, finish):
		return 1


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

