__author__ = 'uhs374h'

from decorator.Decorator import *


class HeisseMilch(Ingredient):
	def getPrice(self):
		return self.drink.getPrice()+0.20

	def __str__(self):
		return str(self.drink)+", Milch"


class MilchSchaum(Ingredient):
	def getPrice(self):
		return self.drink.getPrice()+0.10

	def __str__(self):
		return str(self.drink)+", Milch"


class Schoko(Ingredient):
	def getPrice(self):
		return self.drink.getPrice()+0.10

	def __str__(self):
		return str(self.drink)+", Schoko"


class Soja(Ingredient):
	def getPrice(self):
		return self.drink.getPrice()+0.15

	def __str__(self):
		return str(self.drink)+", Soja"

