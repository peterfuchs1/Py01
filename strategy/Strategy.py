"""
A example for the strategy pattern
This is pure abstract class (interface)
"""
__author__ = 'uhs374h'
from abc import ABCMeta, abstractmethod


class Strategy(object, metaclass=ABCMeta):
	"""Strategy is a pure abstract base class
	"""
	@abstractmethod
	def execute(self, var1, *args):
		""" this method should execute the functionality

		:param var1: numeric or list/tuple of numeric values
		:param args: a tuple of numeric values
		:return: the result
		"""
		pass
	@abstractmethod
	def explaination(self):
		""" explaination of the special strategy
		:return: the explaination as a string
		"""
		pass