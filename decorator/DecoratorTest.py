__author__ = 'uhs374h'

from decorator.Decorators import *


class Espresso(Drink):
	def __init__(self):
		self._description = "Espresso"

	def getPrice(self):
		return 1.99


class HausMischung(Drink):
	def __init__(self):
		self._description = "Hausmischung"

	def getPrice(self):
		return 0.89


if __name__ == "__main__":

	espresso = Espresso()
	spezial = MilchSchaum(Schoko(espresso))
	print(str(spezial)+" %.2f€" % spezial.getPrice())

	hausmischung = HausMischung()
	spezial = Soja(MilchSchaum(Schoko(hausmischung)))
	print(str(spezial)+" %.2f€" % spezial.getPrice())
