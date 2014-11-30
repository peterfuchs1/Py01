__author__ = 'uhs374h'
__name__ = 'Add'
from strategy.Strategy import Strategy


class Add(Strategy):
	""" sum up all values of the given tuple
	"""
	def explaination(self):
		return __name__

	def execute(self, var1=1, *args):
		summe=0
		t=type(var1)
		if t == list or t == tuple:
			summe = sum(var1)
		elif t == int or t == float:
			summe = var1
		else:
			raise TypeError("Wrong type "+t)
		summe += sum(args)
		return summe
