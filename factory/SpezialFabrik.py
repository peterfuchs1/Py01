__author__ = 'uhs374h'

from factory.Produkte import *
from factory.Fabrik import Fabrik


class SpezialFabrik(Fabrik):
	""" This factory can produce all products!

	"""
	@staticmethod
	def erzeuge(product):
		m = globals()  # get the global symbol table as a list
		if product in m:  # do we have this product?
			p = m[product]()  # create a new instance of the product
		else:
			raise TypeError("%s is not implemented yet!" % product)
		return p