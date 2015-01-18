__author__ = 'uhs374h'
from factory.IEinkaufswagen import *
from factory.Artikel import *


class Einkaufswagen(IEinkaufswagen):
	""" A shoping basket

	:ivar paid: Are the products already paid?
	:ivar basket: all selected products
	:ivar shipped: Are the products already shipped?
	:ivar packed: Are the products already packed?
	"""
	def addProduct(self, product):
		"""  add a new product to the basket

		:param product:
		:return:
		"""
		if isinstance(product, Artikel):
			self.basket.append(product)
		else:
			raise TypeError("%s is not a product!" % product)

	def __init__(self):
		""" constructor
		:return:
		"""
		self.paid = False
		self.basket = []
		self.shipped = False
		self.packed = False

	def __str__(self):
		size = len(self.basket)
		out = "Der Einkaufswagen enthaelt %d Produkte:\n" % size
		if size > 0:
			kosten, gewicht = (0.0, 0.0)
			for product in self.basket:
				kosten += product.preis
				gewicht += product.gewicht
				out += product._kategorie + ": Nr. %d" % product.nummer
				out += ", %d%s" % (product.menge, product.mengenEinheit)
				out += " %s, Preis: %.2f\n" % (product.bezeichnung, product.preis)
			out += "Gesamtkosten: %.2f€\n" % kosten
			out += "Gesamtgewicht: %.2fkg\n" % gewicht
			out += "Die Produkte wurden "
			if not self.paid:
				out += "noch nicht "
			out += "bezahlt.\nDie Produkte wurden "
			if not self.packed:
				out += "noch nicht "
			out += "verpackt.\nDie Produkte wurden "
			if not self.shipped:
				out += "noch nicht "
			out += "verschickt.\n\n"

		return out

	def verschicken(self):
		""" shipping your paid products

		:return:
		"""
		if not self.shipped:
			self.shipped = self.packed

	def verpacken(self):
		""" packing your paid products

		:return:
		"""
		if not self.packed:
			self.packed = self.paid

	def bezahlen(self):
		""" pay your basket

		:return:
		"""
		self.paid = True