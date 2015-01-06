__author__ = 'uhs374h'
from factory.Artikel import *


class TiefKuehlProdukt(Artikel):
	def __init__(self, nummer, bezeichnung, preis, menge, mengenEinheit, gewicht):
		super().__init__(nummer, bezeichnung, preis, menge, mengenEinheit, gewicht)
		self._kategorie= "Tiefkuehlware"

class ComputerProdukt(Artikel):
	def __init__(self, nummer, bezeichnung, preis, menge, mengenEinheit, gewicht):
		super().__init__(nummer, bezeichnung, preis, menge, mengenEinheit, gewicht)
		self._kategorie= "Computerware"

