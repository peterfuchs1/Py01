"""
Created on 27.12.2013

@author: uhs374h
"""
from __future__ import division, print_function, unicode_literals


class Bruch(object):

    """ Bruch

    :param int zaehler: numerator
    :param int nenner: denominator
    :ivar int zaehler: numerator
    :ivar int nenner: denominator
    """
    def __iter__(self):

        """make our class iterable
        """
        return (self.zaehler, self.nenner).__iter__()

    def __init__(self, zaehler=0, nenner=1):

        """constructor

        :raise TypeError: incompatible types
        :param zaehler: Bruch or int
        :param nenner: int - not zero
        """
        if isinstance(zaehler, Bruch):
            self.zaehler, self.nenner = zaehler
            return
        elif type(zaehler) is not int:
            raise TypeError('incompatible type:'+type(zaehler).__name__)
        elif type(nenner) is not int:
            raise TypeError('incompatible type:'+type(nenner).__name__) 
        if nenner == 0:
            raise ZeroDivisionError
        self.zaehler = zaehler
        self.nenner = nenner
    
    def __float__(self):

        """overrides float()

        :return: float
        """
        return self.zaehler / self.nenner
    
    def __int__(self):

        """overrides int()

        :return: int
        """
        return int(self.__float__())    
                
    def __neg__(self):

        """negation

        :return: Bruch
        """
        return Bruch(-self.zaehler, self.nenner)
        
    def __radd__(self, zaehler):

        """right version of add

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        return self.__add__(zaehler)
    
    def __add__(self, zaehler):

        """add

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError('incompatible types:'+type(zaehler).__name__+' + Bruch()')        
        nennerneu = self.nenner * n2
        zaehlerneu = z2*self.nenner + n2*self.zaehler
        return Bruch(zaehlerneu, nennerneu)
    
    def __complex__(self):

        """overrides complex()

        :return: complex
        """
        return complex(self.__float__())
        
    def __rsub__(self, left):

        """right version of sub

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        if type(left) is int:
            z2 = left
            nennerneu = self.nenner
            zaehlerneu = z2 * self.nenner - self.zaehler
            return Bruch(zaehlerneu, nennerneu)
        else:
            raise TypeError('incompatible types:' + type(left).__name__+' - Bruch()')

    def __sub__(self, zaehler):

        """sub

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        return self.__add__(zaehler*-1)
    
    def __rmul__(self, zaehler):

        """right version of mul

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        return self.__mul__(zaehler)
        
    def __mul__(self, zaehler):

        """mul

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError('incompatible types:'+type(zaehler).__name__+' * Bruch()')
        z2 *= self.zaehler
        n2 *= self.nenner
        return Bruch(z2, n2)
    
    def __pow__(self, p):

        """Bruch power to self

        :raise TypeError: incompatible types
        :param int p: power
        :return: Bruch
        """
        if type(p) is int:
            return Bruch(self.zaehler**p, self.nenner**p)
        else:
            raise TypeError('incompatible types:'+type(p).__name__+' should be an int')

    def __rdiv__(self, other):

        """
        right version of division for python 2.x

        :param zaehler: int or Bruch
        :return: Bruch
        """
        return self.__rtruediv__(other)
    
    def __rtruediv__(self, left):

        """
        right version of div for python >= 3.x

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        if type(left) is int:
            z2 = left * self.nenner
            if self.zaehler == 0:
                raise ZeroDivisionError
            return Bruch(z2, self.zaehler)
        else:
            raise TypeError('incompatible types:'+type(left).__name__+' / Bruch()')

    def __div__(self, other):

        """
        division for python 2.x

        :param other: int or Bruch
        :return: Bruch
        """
        return self.__truediv__(other)

    def __truediv__(self, zaehler):

        """
        division python >= 3.x

        :raise TypeError: incompatible types
        :param zaehler: Bruch or int
        :return: Bruch
        """
        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError('incompatible types:'+type(zaehler).__name__+' / Bruch()')
        if z2 == 0:
            raise ZeroDivisionError
        return self.__mul__(Bruch(n2, z2))
    
    def __invert__(self):

        """
        invert a Bruch ~

        :return: Bruch
        """
        return Bruch(self.nenner, self.zaehler)

    def __repr__(self):

        """
        representation of the Bruch object

        :return str: the representation
        """
        # Vor der Ausgabe wird gekuerzt!
        shorten = Bruch.gcd(self.zaehler, self.nenner)
        self.zaehler //= shorten
        self.nenner //= shorten
        # Nenner stehts positiv
        if self.nenner < 0:
            self.nenner *= -1
            self.zaehler *= -1
            
        if self.nenner == 1:
            return "(%d)" % self.zaehler
        else:
            return "(%d/%d)" % (self.zaehler, self.nenner)
    
    @staticmethod  # not necessary in python >= 3.x
    def __makeBruch(other):

        """make a Bruch for sure

        :raise TypeError: incompatible types
        :param other: Bruch or int
        :return: Bruch
        """
        '''create a Bruch from int or return the reference'''
        if isinstance(other, Bruch):
            return other
        elif type(other) is int:
            b = Bruch(other, 1)
            return b
        else:
            raise TypeError('incompatible types:'+type(other).__name__+' not an int nor a Bruch')
    
    def __eq__(self, other):

        """equal to

        :param Bruch other: other Bruch
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner == other.zaehler * self.nenner
        
    def __ne__(self, other):

        """not equal to

        :param Bruch other: other Bruch
        :return: boolean
        """
        return not self.__eq__(other)
    
    def __gt__(self, other):

        """greather than

        :param Bruch other: other Bruch
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner > other.zaehler * self.nenner
        
    def __lt__(self, other):

        """lower than

        :param Bruch other: other Bruch
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner < other.zaehler * self.nenner
        
    def __ge__(self, other):
        """greather or equal to

        :param Bruch other: other Bruch
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner >= other.zaehler * self.nenner
        
    def __le__(self, other):
        """lower or equal to

        :param Bruch other: other Bruch
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner <= other.zaehler * self.nenner
    
    def __abs__(self):
        """abs(Bruch)

        :return: positive Bruch
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))
    
    def __iadd__(self, other):

        """intern add

        :param Bruch other: Bruch
        :return: self
        """
        other = Bruch.__makeBruch(other)
        self = self + other
        return self
        
    def __isub__(self, other):

        """intern sub

        :param Bruch other: Bruch
        :return: self
        """
        other = Bruch.__makeBruch(other)
        self = self - other
        return self
        
    def __imul__(self, other):

        """intern mul

        :param Bruch other: other Bruch
        :return: self
        """
        other = Bruch.__makeBruch(other)
        self = self * other
        return self
    
    def __idiv__(self, other):

        """intern division 2.x

        :param Bruch other: other Bruch
        :return: self
        """
        return self.__itruediv__(other)

    def __itruediv__(self, other):

        """intern division 3.x

        :param Bruch other: other Bruch
        :return: self
        """
        other = Bruch.__makeBruch(other)
        self = self / other
        return self
        
    @classmethod
    def gcd(cls, x, y):

        """euclid's algorithm

        :param int x: first value
        :param int y: second value
        :return: greatest common divisor
        """
        x, y = abs(x), abs(y)  # positive Werte!!
        if x < y:
            x, y = y, x
        """Berechnung """
        while y != 0:
            x, y = y, x % y
        return x
