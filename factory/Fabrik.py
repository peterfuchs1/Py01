__author__ = 'uhs374h'
from abc import ABCMeta


class Fabrik(metaclass=ABCMeta):
	""" This is the base class of all factories

	:ivar _fabArt: which products can be produced?
	"""

	def __init__(self):
		self._fabArt = "unbekannt"

	@staticmethod
	def erzeuge(product):
		""" produce a special pruduct

		:param product: product to produce
		:return:
		"""
		pass
