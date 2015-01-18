__author__ = 'uhs374h'
from factory.Artikel import *


class TiefKuehlProdukt(Artikel):
	""" Create deep frozen products

	"""
	def __init__(self, nummer, bezeichnung, preis, menge, mengenEinheit, gewicht):
		super().__init__(nummer, bezeichnung, preis, menge, mengenEinheit, gewicht)
		self._kategorie= "Tiefkuehlware"


class ComputerProdukt(Artikel):
	""" Create computer products

	"""
	def __init__(self, nummer, bezeichnung, preis, menge, mengenEinheit, gewicht):
		super().__init__(nummer, bezeichnung, preis, menge, mengenEinheit, gewicht)
		self._kategorie= "Computerware"

