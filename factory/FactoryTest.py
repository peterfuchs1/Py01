__author__ = 'uhs374h'
from factory import *

if __name__ == "__main__":
	spinat = SpezialFabrik.erzeuge("TKSpinat")
	maroni1 = SpezialFabrik.erzeuge("Maronireis")
	maroni2 = SpezialFabrik.erzeuge("Maronireis")
	usb = SpezialFabrik.erzeuge("USB_Stick")
	ekw = Einkaufswagen()
	ekw.addProduct(spinat)
	ekw.addProduct(maroni1)
	ekw.addProduct(maroni2)
	ekw.addProduct(usb)
	print(ekw)
	ekw.bezahlen()
	print(ekw)
	ekw.verpacken()
	ekw.verschicken()
	print(ekw)
	try:
		produkt = "Elefant"
		SpezialFabrik.erzeuge(produkt)
	except TypeError:
		print("Das Produkt [%s] ist noch nicht verfügbar!" % produkt)