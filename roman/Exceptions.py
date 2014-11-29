__author__ = 'uhs374h'
"""Define exceptions

"""


class RomanError(Exception):
	pass


class OutOfRangeError(RomanError):
	pass


class NotIntegerError(RomanError):
	pass


class InvalidRomanNumeralError(RomanError):
	pass