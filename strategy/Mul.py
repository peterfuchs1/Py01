__author__ = 'uhs374h'
__name__ = 'Mul'
from strategy.Strategy import Strategy


class Mul(Strategy):
	""" multiply up all values of the given tuple
	"""
	def explaination(self):
		return __name__

	def execute(self, var1=1, *args):
		t = type(var1)
		mul=0
		if t == list or t == tuple:
			mul = var1[0]
			for x in var1[1:]:
				mul *= x
		elif t == int or t == float:
			mul = var1
		else:
			raise TypeError("Wrong type "+str(t))
		for x in args:
			mul *= x
		return mul
