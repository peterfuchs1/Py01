__author__ = 'uhs374h'
__name__ = 'Mod'
from strategy.Strategy import Strategy


class Mod(Strategy):
	""" modulo up all values of the given tuple
	"""
	def explaination(self):
		return __name__

	def execute(self, var1=1, *args):
		t = type(var1)
		div = 0
		if t == list or t == tuple:
			div = var1[0]
			for x in var1[1:]:
				if x == 0:
					raise ZeroDivisionError
				div %= x
		elif t == int or t == float:
			div = var1
		else:
			raise TypeError("Wrong type "+str(t))
		for x in args:
			if x == 0:
				raise ZeroDivisionError
			div %= x

		return div
