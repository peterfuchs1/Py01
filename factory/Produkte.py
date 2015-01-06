__author__ = 'uhs374h'

from factory.Kategorien import *
from factory.Artikel import *

class USB_Stick(ComputerProdukt):
	def __init__(self, nummer=1, bezeichnung="USB_16_GB", preis=9.99, menge=1, mengenEinheit=Einheiten.STK, gewicht=0.2):
		super().__init__(nummer, bezeichnung, preis, menge, mengenEinheit, gewicht)

class Maronireis(TiefKuehlProdukt):
	def __init__(self, nummer=123, bezeichnung="Maronireis", preis=0.99, menge=500, mengenEinheit=Einheiten.G, gewicht=0.6):
		super().__init__(nummer, bezeichnung, preis, menge, mengenEinheit, gewicht)

class TKSpinat(TiefKuehlProdukt):
	def __init__(self, nummer=99, bezeichnung="Tiefkuehl Spinat", preis=1.49, menge=250, mengenEinheit=Einheiten.G, gewicht=0.3):
		super().__init__(nummer, bezeichnung, preis, menge, mengenEinheit, gewicht)

