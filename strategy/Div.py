__author__ = 'uhs374h'
__name__ = 'Div'
from strategy.Strategy import Strategy


class Div(Strategy):
	""" sum up all values of the given tuple
	"""
	def explaination(self):
		return __name__

	def execute(self, *args):
		liste = args[0]
		div = liste[0]
		for x in liste[1:]:
			div /= x
		return div
