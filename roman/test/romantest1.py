"""Unit test for roman.py

This program is part of "Dive Into Python", a free Python book for
experienced programmers.  Visit http://diveintopython.org/ for the
latest version.
"""

__author__ = "Mark Pilgrim (mark@diveintopython.org)"
__version__ = "$Revision: 1.3 $"
__date__ = "$Date: 2004/05/05 21:57:20 $"
__copyright__ = "Copyright (c) 2001 Mark Pilgrim"
__license__ = "Python"


from roman.roman import Roman
from roman.Exceptions import InvalidRomanNumeralError, NotIntegerError, OutOfRangeError

import unittest


class KnownValues(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.r = Roman()

    knownValues = ((1, 'I'),
                   (2, 'II'),
                   (3, 'III'),
                   (4, 'IV'),
                   (5, 'V'),
                   (6, 'VI'),
                   (7, 'VII'),
                   (8, 'VIII'),
                   (9, 'IX'),
                   (10, 'X'),
                   (50, 'L'),
                   (100, 'C'),
                   (500, 'D'),
                   (1000, 'M'),
                   (31, 'XXXI'),
                   (148, 'CXLVIII'),
                   (294, 'CCXCIV'),
                   (312, 'CCCXII'),
                   (421, 'CDXXI'),
                   (528, 'DXXVIII'),
                   (621, 'DCXXI'),
                   (782, 'DCCLXXXII'),
                   (870, 'DCCCLXX'),
                   (941, 'CMXLI'),
                   (1043, 'MXLIII'),
                   (1110, 'MCX'),
                   (1226, 'MCCXXVI'),
                   (1301, 'MCCCI'),
                   (1485, 'MCDLXXXV'),
                   (1509, 'MDIX'),
                   (1607, 'MDCVII'),
                   (1754, 'MDCCLIV'),
                   (1832, 'MDCCCXXXII'),
                   (1993, 'MCMXCIII'),
                   (2074, 'MMLXXIV'),
                   (2152, 'MMCLII'),
                   (2212, 'MMCCXII'),
                   (2343, 'MMCCCXLIII'),
                   (2499, 'MMCDXCIX'),
                   (2574, 'MMDLXXIV'),
                   (2646, 'MMDCXLVI'),
                   (2723, 'MMDCCXXIII'),
                   (2892, 'MMDCCCXCII'),
                   (2975, 'MMCMLXXV'),
                   (3051, 'MMMLI'),
                   (3185, 'MMMCLXXXV'),
                   (3250, 'MMMCCL'),
                   (3313, 'MMMCCCXIII'),
                   (3408, 'MMMCDVIII'),
                   (3501, 'MMMDI'),
                   (3610, 'MMMDCX'),
                   (3743, 'MMMDCCXLIII'),
                   (3844, 'MMMDCCCXLIV'),
                   (3888, 'MMMDCCCLXXXVIII'),
                   (3940, 'MMMCMXL'),
                   (3999, 'MMMCMXCIX'))

    def testToRomanKnownValues(self):
        """toRoman should give known result with known input"""
        for integer, numeral in self.knownValues:
            result = self.r.toRoman(integer)
            self.assertEqual(numeral, result)

    def testFromRomanKnownValues(self):
        """fromRoman should give known result with known input"""
        for integer, numeral in self.knownValues:
            result = self.r.fromRoman(numeral)
            self.assertEqual(integer, result)


class Singleton(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.r = Roman()

    def testSingleton(self):
        self.r2 = Roman()
        self.assertTrue(id(self.r) == id(self.r2))


class ToRomanBadInput(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.r = Roman()

    def testTooLarge(self):
        """toRoman should fail with large input"""
        self.assertRaises(OutOfRangeError, self.r.toRoman, 5000)

    def testZero(self):
        """toRoman should fail with 0 input"""
        self.assertRaises(OutOfRangeError, self.r.toRoman, 0)

    def testNegative(self):
        """toRoman should fail with negative input"""
        self.assertRaises(OutOfRangeError, self.r.toRoman, -1)

    def testNonInteger(self):
        """toRoman should fail with non-integer input"""
        self.assertRaises(NotIntegerError, self.r.toRoman, 0.5)


class FromRomanBadInput(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.r = Roman()

    def testTooManyRepeatedNumerals(self):
        """fromRoman should fail with too many repeated numerals"""
        for s in ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(InvalidRomanNumeralError, self.r.fromRoman, s)

    def testRepeatedPairs(self):
        """fromRoman should fail with repeated pairs of numerals"""
        for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
            self.assertRaises(InvalidRomanNumeralError, self.r.fromRoman, s)

    def testMalformedAntecedent(self):
        """fromRoman should fail with malformed antecedents"""
        for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                  'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(InvalidRomanNumeralError, self.r.fromRoman, s)


class SanityCheck(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.r = Roman()

    def testSanity(self):
        """fromRoman(toRoman(n))==n for all n"""
        for integer in range(1, 4000):
            numeral = self.r.toRoman(integer)
            result = self.r.fromRoman(numeral)
            self.assertEqual(integer, result)


class CaseCheck(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.r = Roman()

    def testToRomanCase(self):
        """toRoman should always return uppercase"""
        for integer in range(1, 4000):
            numeral = self.r.toRoman(integer)
            self.assertEqual(numeral, numeral.upper())

    def testFromRomanCase(self):
        """fromRoman should only accept uppercase input"""
        for integer in range(1, 4000):
            numeral = self.r.toRoman(integer)
            self.r.fromRoman(numeral.upper())
            self.assertRaises(InvalidRomanNumeralError,
                              self.r.fromRoman, numeral.lower())

if __name__ == "__main__":
    unittest.main()
