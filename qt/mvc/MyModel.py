__author__ = 'uhs374h'

class MyModel(object):
	""" Model within the MVC-pattern
	"""
	def __init__(self, size):
		self.size = size
		self.open = size
		self.correct = 0
		self.wrong = 0
		self.sum = 0
		self.games = 0

	def newGame(self):
		self.open = self.size
		self.correct = 0
		self.wrong = 0
		self.sum = 0
		self.games += 1

	def correctClick(self):
		self.open -= 1
		self.correct += 1
		self.sum += 1

	def wrongClick(self):
		self.wrong += 1
		self.sum += 1

	def openStr(self):
		return str(self.open)

	def correctStr(self):
		return str(self.correct)

	def wrongStr(self):
		return str(self.wrong)

	def gamesStr(self):
		return str(self.games)

	def sumStr(self):
		return str(self.sum)
