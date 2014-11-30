__author__ = 'uhs374h'
from strategy import *
import unittest


class MyAddCase(unittest.TestCase):

	def setUp(self):
		super().setUp()
		self.algorithm = (Add(), Sub())

	def test_ADD(self):

		liste = [x for x in range(1, 11)]
		expected = sum(liste)
		self.assertEqual(expected, self.algorithm[0].execute(liste))

	def test_Add_simpleTuple(self):
		liste = (3,4)
		expected = sum(liste)
		self.assertEqual(expected, self.algorithm[0].execute(liste))

	def test_Add_3_parameter(self):
		a, b, c = 2, 3, 4
		expected = sum((a, b, c))
		self.assertEqual(expected, self.algorithm[0].execute((a, b, c)))


class MySubCase(unittest.TestCase):

	def setUp(self):
		super().setUp()
		self.algorithm = (Add(), Sub())

	def test_Sub(self):

		liste = [x for x in range(1, 11)]
		diff = liste[0]
		for x in liste[1:]:
			diff -= x
		expected = diff
		self.assertEqual(expected, self.algorithm[1].execute(liste))

	def test_Sub_simpleTuple(self):
		liste = (3, 4)
		expected = liste[0] - liste[1]
		self.assertEqual(expected, self.algorithm[1].execute(liste))

	def test_Sub_3_parameter(self):
		a, b, c = 2, 3, 4
		expected = a-b-c
		self.assertEqual(expected, self.algorithm[1].execute((a, b, c)))


class MyMulCase(unittest.TestCase):

	def setUp(self):
		super().setUp()
		self.algorithm = (Add(), Sub(), Mul())

	def test_Mul(self):

		liste = [x for x in range(1, 11)]
		mul = liste[0]
		for x in liste[1:]:
			mul *= x
		expected = mul
		self.assertEqual(expected, self.algorithm[2].execute(liste))

	def test_Mul_simpleTuple(self):
		liste = (3,4)
		expected = liste[0]*liste[1]
		self.assertEqual(expected, self.algorithm[2].execute(liste))

	def test_Mul_3_parameter(self):
		a, b, c = 2, 3, 4
		expected = a*b*c
		self.assertEqual(expected, self.algorithm[2].execute((a, b, c)))


class MyDivCase(unittest.TestCase):

	def setUp(self):
		super().setUp()
		self.algorithm = (Add(), Sub(), Mul(), Div())

	def test_Div(self):

		liste = [x for x in range(1, 11)]
		div = liste[0]
		for x in liste[1:]:
			div /= x
		expected = div
		self.assertEqual(expected, self.algorithm[3].execute(liste))

	def test_Div_simpleTuple(self):
		liste = (3,4)
		expected = liste[0]/liste[1]
		self.assertEqual(expected, self.algorithm[3].execute(liste))

	def test_Div_3_parameter(self):
		a, b, c = 2, 3, 4
		expected = a/b/c
		self.assertEqual(expected, self.algorithm[3].execute((a, b, c)))


class MyModCase(unittest.TestCase):

	def setUp(self):
		super().setUp()
		self.algorithm = (Add(), Sub(), Mul(), Div(), Mod())

	def test_Mod(self):

		liste = [x for x in range(1, 11)]
		div = liste[0]
		for x in liste[1:]:
			div %= x
		expected = div
		self.assertEqual(expected, self.algorithm[4].execute(liste))

	def test_Mod_simpleTuple(self):
		liste = (3, 4)
		expected = divmod(liste[0], liste[1])
		self.assertEqual(expected, self.algorithm[4].execute(liste))

	def test_Mod_3_parameter(self):
		a, b, c = 4, 3, 2
		expected = a % b
		expected %= c
		self.assertEqual(expected, self.algorithm[4].execute((a, b, c)))

if __name__ == '__main__':
	unittest.main()
