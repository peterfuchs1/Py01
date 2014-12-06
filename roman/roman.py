"""Convert to and from Roman numerals

This program is part of "Dive Into Python", a free Python book for
experienced programmers.  Visit http://diveintopython.org/ for the
latest version.
"""

__author__ = "Mark Pilgrim (mark@diveintopython.org)"
__version__ = "$Revision: 1.2 $"
__date__ = "$Date: 2004/05/05 21:57:20 $"
__copyright__ = "Copyright (c) 2001 Mark Pilgrim"
__license__ = "Python"

from roman.Exceptions import *


class Roman(object):
    """Roman numbers representation

    """
    __instance = None
    def __new__(cls, val=None):
        """We want only one instance!

        :param cls:
        :param val:
        :return:
        """
        if Roman.__instance is None:
            Roman.__instance = object.__new__(cls)
            Roman.fillLookupTables()
        Roman.__instance.val = val
        return Roman.__instance

#Create tables for fast conversion of roman numerals.
#See fillLookupTables() below.
    toRomanTable = [ None ]  # Skip an index since Roman numerals have no zero
    fromRomanTable = {}


#Roman numerals must be less than 4000
    MAX_ROMAN_NUMERAL = 3999

#Define digit mapping
    romanNumeralMap = (('M',  1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I',  1))

    @staticmethod
    def toRoman(n):
        """convert integer to Roman numeral"""
        if not (0 < n <= Roman.MAX_ROMAN_NUMERAL):
            raise OutOfRangeError("number out of range (must be 1..4999)")
        if int(n) != n:
            raise NotIntegerError("non-integers can not be converted")
        return Roman.toRomanTable[n]
    @staticmethod
    def fromRoman(s):
        """convert Roman numeral to integer"""
        if not s:
            raise InvalidRomanNumeralError ('Input can not be blank')
        if not s in Roman.fromRomanTable:
            raise InvalidRomanNumeralError ('Invalid Roman numeral: %s' % s)
        return Roman.fromRomanTable[s]
    @staticmethod
    def toRomanDynamic(n):
        """convert integer to Roman numeral using dynamic programming"""
        assert(0 < n <= Roman.MAX_ROMAN_NUMERAL)
        assert(int(n) == n)
        result = ""
        for numeral, integer in Roman.romanNumeralMap:
            if n >= integer:
                result = numeral
                n -= integer
                break
        if n > 0:
            result += Roman.toRomanTable[n]
        return result
    @staticmethod
    def fillLookupTables():
        """compute all the possible roman numerals"""
        #Save the values in two global tables to convert to and from integers.
        for integer in range(1, Roman.MAX_ROMAN_NUMERAL + 1):
            romanNumber = Roman.toRomanDynamic(integer)
            Roman.toRomanTable.append(romanNumber)
            Roman.fromRomanTable[romanNumber] = integer
    def __init__(self):
        pass