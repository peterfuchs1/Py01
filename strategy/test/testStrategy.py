__author__ = 'uhs374h'
from strategy import *
import unittest


class MyAddCase(unittest.TestCase):

	def setUp(self):
		super().setUp()
		self.algorithm = (Add(), Sub())

	def test_ADD_explaination(self):
		expected = "Add"
		self.assertEqual(expected, self.algorithm[0].explaination())

	def test_ADD(self):

		liste = [x for x in range(1, 11)]
		expected = sum(liste)
		self.assertEqual(expected, self.algorithm[0].execute(liste))

	def test_Add_simpleTuple(self):
		liste = (3, 4)
		expected = sum(liste)
		self.assertEqual(expected, self.algorithm[0].execute(liste))

	def test_Add_floatTuple(self):
		liste = (3.0, 4.0)
		expected = sum(liste)
		self.assertEqual(expected, self.algorithm[0].execute(liste))

	def test_Add_float_Parameter(self):
		x, y = (3.0, 4.0)
		expected = x + y
		self.assertEqual(expected, self.algorithm[0].execute(x, y))

	def test_Add_3_parameter(self):
		a, b, c = 2, 3, 4
		expected = sum((a, b, c))
		self.assertEqual(expected, self.algorithm[0].execute((a, b, c)))

	def test_Add_WrongType(self):
		self.assertRaises(TypeError, self.algorithm[0].execute, "String")


class MySubCase(unittest.TestCase):

	def setUp(self):
		super().setUp()
		self.algorithm = (Add(), Sub())

	def test_Sub_explaination(self):
		expected = "Sub"
		self.assertEqual(expected, self.algorithm[1].explaination())

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

	def test_Sub_floatTuple(self):
		liste = (3.0, 4.0)
		expected = liste[0] - liste[1]
		self.assertEqual(expected, self.algorithm[1].execute(liste))

	def test_Sub_float_Parameter(self):
		x, y = (3.0, 4.0)
		expected = x - y
		self.assertEqual(expected, self.algorithm[1].execute(x, y))

	def test_Sub_3_parameter(self):
		a, b, c = 2, 3, 4
		expected = a-b-c
		self.assertEqual(expected, self.algorithm[1].execute((a, b, c)))

	def test_Sub_WrongType(self):
		self.assertRaises(TypeError, self.algorithm[1].execute, "String")


class MyMulCase(unittest.TestCase):

	def setUp(self):
		super().setUp()
		self.algorithm = (Add(), Sub(), Mul())

	def test_Mul_explaination(self):
		expected = "Mul"
		self.assertEqual(expected, self.algorithm[2].explaination())

	def test_Mul(self):

		liste = [x for x in range(1, 11)]
		mul = liste[0]
		for x in liste[1:]:
			mul *= x
		expected = mul
		self.assertEqual(expected, self.algorithm[2].execute(liste))

	def test_Mul_simpleTuple(self):
		liste = (3, 4)
		expected = liste[0]*liste[1]
		self.assertEqual(expected, self.algorithm[2].execute(liste))

	def test_Mul_floatTuple(self):
		liste = (3.0, 4.0)
		expected = liste[0] * liste[1]
		self.assertEqual(expected, self.algorithm[2].execute(liste))

	def test_Mul_float_Parameter(self):
		x, y = (3.0, 4.0)
		expected = x * y
		self.assertEqual(expected, self.algorithm[2].execute(x, y))

	def test_Mul_3_parameter(self):
		a, b, c = 2, 3, 4
		expected = a*b*c
		self.assertEqual(expected, self.algorithm[2].execute((a, b, c)))

	def test_Mul_WrongType(self):
		self.assertRaises(TypeError, self.algorithm[2].execute, "String")



class MyDivCase(unittest.TestCase):

	def setUp(self):
		super().setUp()
		self.algorithm = (Add(), Sub(), Mul(), Div())

	def test_Div_explaination(self):
		expected = "Div"
		self.assertEqual(expected, self.algorithm[3].explaination())

	def test_Div(self):
		liste = [x for x in range(1, 11)]
		div = liste[0]
		for x in liste[1:]:
			div /= x
		expected = div
		self.assertEqual(expected, self.algorithm[3].execute(liste))

	def test_Div_simple_2_Arguments(self):
		x, y = (3, 4)
		expected = x / y
		self.assertEqual(expected, self.algorithm[3].execute(x,y))

	def test_Div_3_parameter(self):
		a, b, c = 2, 3, 4
		expected = a/b/c
		self.assertEqual(expected, self.algorithm[3].execute((a, b, c)))

	def test_Div_simpleTuple(self):
		liste = (3, 4)
		expected = liste[0]/liste[1]
		self.assertEqual(expected, self.algorithm[3].execute(liste))

	def test_Div_floatTuple(self):
		liste = (3.0, 4.0)
		expected = liste[0]/liste[1]
		self.assertEqual(expected, self.algorithm[3].execute(liste))

	def test_Div_simpleTuple_DbyZero(self):
		liste = (3, 0)
		self.assertRaises(ZeroDivisionError, self.algorithm[3].execute, liste)

	def test_Div_simple_2_int_Arguments_last_0(self):
		x, y = (3, 0)
		self.assertRaises(ZeroDivisionError, self.algorithm[3].execute, x, y)

	def test_Div_simple_2_float_Arguments_last_0(self):
		x, y = (3.0, 0.0)
		self.assertRaises(ZeroDivisionError, self.algorithm[3].execute, x, y)

	def test_Div_3_parameter_DbyZero(self):
		a, b, c = 2, 0, 4
		self.assertRaises(ZeroDivisionError, self.algorithm[3].execute, a, b, c)

	def test_Div_3_parameter_DbyZero_lastArgument(self):
		a, b, c = 2, 3, 0
		self.assertRaises(ZeroDivisionError, self.algorithm[3].execute, a, b, c)

	def test_Div_WrongType(self):
		self.assertRaises(TypeError, self.algorithm[3].execute, "String")


class MyModCase(unittest.TestCase):

	def setUp(self):
		super().setUp()
		self.algorithm = (Add(), Sub(), Mul(), Div(), Mod())

	def test_Mod_explaination(self):
		expected = "Mod"
		self.assertEqual(expected, self.algorithm[4].explaination())

	def test_Mod(self):
		liste = [x for x in range(1, 11)]
		div = liste[0]
		for x in liste[1:]:
			div %= x
		expected = div
		self.assertEqual(expected, self.algorithm[4].execute(liste))

	def test_Mod_simpleTuple(self):
		liste = (3, 4)
		expected = liste[0] % liste[1]
		self.assertEqual(expected, self.algorithm[4].execute(liste))

	def test_Mod_3_parameter(self):
		a, b, c = 4, 3, 2
		expected = a % b
		expected %= c
		self.assertEqual(expected, self.algorithm[4].execute((a, b, c)))

	def test_Mod_simpleTuple_DbyZero(self):
		liste = (3, 0)
		self.assertRaises(ZeroDivisionError, self.algorithm[4].execute, liste)

	def test_Mod_simple_2_Arguments_last_0(self):
		x, y = (3, 0)
		self.assertRaises(ZeroDivisionError, self.algorithm[4].execute, x, y)

	def test_Mod_3_parameter_DbyZero(self):
		a, b, c = 2, 0, 4
		self.assertRaises(ZeroDivisionError, self.algorithm[4].execute, a, b, c)

	def test_Mod_3_parameter_DbyZero_lastArgument(self):
		a, b, c = 2, 3, 0
		self.assertRaises(ZeroDivisionError, self.algorithm[4].execute, a, b, c)

	def test_Mod_WrongType(self):
		self.assertRaises(TypeError, self.algorithm[4].execute, "String")


if __name__ == '__main__':
	unittest.main()
