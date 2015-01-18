__author__ = 'uhs374h'

from abc import ABCMeta, abstractmethod


class IEinkaufswagen (object, metaclass=ABCMeta):
	""" The pure abstract base class of all baskets

	"""
	@abstractmethod
	def addProduct(self, product):
		"""  add a new product to the basket

		:param product: a product
		:return:
		"""
		pass

	@abstractmethod
	def bezahlen(self):
		""" pay your basket

		:return:
		"""
		pass

	@abstractmethod
	def verpacken(self):
		""" packing your paid products

		:return:
		"""
		pass

	@abstractmethod
	def verschicken(self):
		""" shipping your paid products

		:return:
		"""
		pass

	@abstractmethod
	def __str__(self):
		""" convert the status into a string

		:return:
		"""
		pass