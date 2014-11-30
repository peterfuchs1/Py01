__author__ = 'uhs374h'
__name__ = 'Sub'
from strategy.Strategy import Strategy


class Sub(Strategy):
	""" subtract all values of the given tuple
	"""
	def explaination(self):
		return __name__

	def execute(self, *args):
		liste = args[0]
		diff = liste[0]
		for x in liste[1:]:
			diff -= x
		return diff
