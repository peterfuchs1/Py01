__author__ = 'uhs374h'
from abc import ABCMeta


class Einheiten:
	""" units of our products

	"""
	STK = "stk"
	M = "m"
	KG = "kg"
	L = "l"
	G = "g"
	ML = "ml"


class Artikel(metaclass=ABCMeta):
	""" this is the abstract base class of all products

	"""
	def __init__(self, nummer, bezeichnung, preis,
	             menge=1, mengenEinheit=Einheiten.STK, gewicht=1):
		self.nummer = nummer
		self.bezeichnung = bezeichnung
		self.preis = preis
		self.menge = menge
		self.mengenEinheit = mengenEinheit
		self.gewicht = gewicht
		self._kategorie = None
