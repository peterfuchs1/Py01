__author__ = 'uhs374h'
__name__ = 'Mul'
from strategy.Strategy import Strategy


class Mul(Strategy):
	""" sum up all values of the given tuple
	"""
	def explaination(self):
		return __name__

	def execute(self, *args):
		liste = args[0]
		mul = liste[0]
		for x in liste[1:]:
			mul *= x
		return mul
