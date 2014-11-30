__author__ = 'uhs374h'
__name__ = 'Add'
from strategy.Strategy import Strategy


class Add(Strategy):
	""" sum up all values of the given tuple
	"""
	def explaination(self):
		return __name__

	def execute(self, *args):
		return sum(*args)
