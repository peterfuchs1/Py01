__author__ = 'uhs374h'
__name__ = 'Sub'
from strategy.Strategy import Strategy


class Sub(Strategy):
	""" subtract all values of the given tuple
	"""
	def explaination(self):
		return __name__

	def execute(self, var1=1, *args):
		t = type(var1)
		diff = 0
		if t == list or t == tuple:
			diff = var1[0]
			for x in var1[1:]:
				diff -= x
		elif t == int or t == float:
			diff = var1
		else:
			raise TypeError("Wrong type "+str(t))
		for x in args:
			diff -= x
		return diff
