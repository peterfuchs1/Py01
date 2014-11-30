__author__ = 'uhs374h'
from abc import ABCMeta


class Strategy(metaclass=ABCMeta):

	def execute(self, *args):
		pass

	def explaination(self):
		pass