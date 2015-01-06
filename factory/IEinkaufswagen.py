__author__ = 'uhs374h'

from abc import ABCMeta, abstractmethod


class IEinkaufswagen (object, metaclass=ABCMeta):
	@abstractmethod
	def addProduct(self, product):
		"""  add a new product to the basket

		:param product:
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
		pass