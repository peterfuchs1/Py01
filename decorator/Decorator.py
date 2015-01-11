__author__ = 'uhs374h'
from abc import abstractmethod, ABCMeta


class Drink(metaclass=ABCMeta):

	def __init__(self):
		self._description = "unknown drink"

	def __str__(self):
		""" A useful description for the drink

		:return: a string representation for the drink
		"""
		return self._description

	@abstractmethod
	def getPrice(self):
		""" A calculation for the drink

		:return: the total cost of the drink
		"""

class Ingredient (Drink, metaclass=ABCMeta):
	def __init__(self, drink):
		self.drink = drink

	@abstractmethod
	def __str__(self):
		""" A useful description for the drink

		:return: a string representation for the drink
		"""
