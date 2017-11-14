"""
module rational number
"""

def _gcd(num_a, num_b):
    """
    gratest common divisor
    """
    if num_a == 0 or num_b == 0:
        raise ArithmeticError('gcd of zero')
    var_p = num_a
    var_q = num_b
    if var_p < var_q:
        var_p = num_b
        var_q = num_a
    var_r = var_p % var_q
    while var_r != 0:
        var_p = var_q
        var_q = var_r
        var_r = var_p % var_q
    return var_q

class Rational(object):
    """
    representing rational number
    """
    def __init__(self, num, den):
        """
        simple constructor
        """
        if den == 0:
            raise ZeroDivisionError('division by zero')
        if num == 0:
            self._num = 0
            self._den = 1
        else:
            sign = 1
            if num * den < 0:
                sign = -1
            abs_num = abs(num)
            abs_den = abs(den)
            divisor = _gcd(abs_num, abs_den)
            self._num = sign * abs_num // divisor
            self._den = abs_den // divisor
    #
    def __add__(self, other):
        """
        '+' operator
        """
        # supported type for operand except Rational
        if isinstance(other, int):
            return Rational(self.num + self.den * other, self.den)
        if not isinstance(other, Rational):
            return NotImplemented
        return Rational(self.num * other.den + self.den * other.num, self.den * other.den)
    def __radd__(self, other):
        """
        fallback of '+' operator
        """
        if isinstance(other, int):
            return self.__add__(other)
        return NotImplemented
    #
    def __sub__(self, other):
        """
        '-' binary operator
        """
        # supported type for operand except Rational
        if isinstance(other, int):
            return Rational(self.num - self.den * other, self.den)
        if not isinstance(other, Rational):
            return NotImplemented
        return Rational(self.num * other.den - self.den * other.num, self.den * other.den)
    def __rsub__(self, other):
        """
        fallback of '-' binary operator
        """
        if isinstance(other, int):
            return self.__neg__().__add__(- other)
        return NotImplemented
    #
    def __mul__(self, other):
        """
        '*' operator
        """
        # supported type for operand except Rational
        if isinstance(other, int):
            return Rational(self.num * other, self.den)
        if not isinstance(other, Rational):
            return NotImplemented
        return Rational(self.num * other.num, self.den * other.den)
    def __rmul__(self, other):
        """
        fallback of '*' operator
        """
        return self.__mul__(other)
    #
    def __truediv__(self, other):
        """
        '/' operator when '__future__.division' is in effect
        """
        # supported type for operand except Rational
        if isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError('division by zero')
            return Rational(self.num, self.den * other)
        if not isinstance(other, Rational):
            return NotImplemented
        if other == 0:
            raise ZeroDivisionError('division by zero')
        return Rational(self.num * other.den, self.den * other.num)
    def __rtruediv__(self, other):
        """
        fallback of '/' operator when '__future__.division' is in effect
        """
        if isinstance(other, int):
            return Rational(self.den * other, self.num)
        return NotImplemented
    #
    def __floordiv__(self, other):
        """
        '//' operator
        """
        return self.__truediv__(other)
    def __rfloordiv__(self, other):
        """
        fallback of '//' operator
        """
        return self.__rtruediv__(other)
    #
    def __div__(self, other):
        """
        '/' operator
        """
        return self.__truediv__(other)
    def __rdiv__(self, other):
        """
        fallback of '/' operator
        """
        return self.__rtruediv__(other)
    #
    def __mod__(self, other):
        """
        '%' operator
        """
        if isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError('division by zero')
            return Rational(0, 1)
        if not isinstance(other, Rational):
            return NotImplemented
        if other == 0:
            raise ZeroDivisionError('division by zero')
        return Rational(0, 1)
    def __rmod__(self, other):
        """
        fallback of '%' operator
        """
        if self == Rational(0, 1):
            raise ZeroDivisionError('division by zero')
        return Rational(0, 1)
    #
    def __divmod__(self, other):
        """
        'divmod()' operation
        """
        quot = self.__floordiv__(other)
        res = self.__mod__(other)
        if quot != NotImplemented and res != NotImplemented:
            return (quot, res)
        return NotImplemented
    def __rdivmod__(self, other):
        """
        fallback of 'divmod()' operation
        """
        quot = self.__rfloordiv__(other)
        res = self.__rmod__(other)
        if quot != NotImplemented and res != NotImplemented:
            return (quot, res)
        return NotImplemented
    #
    def __pos__(self):
        """
        '+' unary operator
        """
        return self
    #
    def __neg__(self):
        """
        '-' unary operator
        """
        return Rational(-1 * self.num, self.den)
    #
    def __abs__(self):
        """
        absolute value
        """
        return Rational(abs(self.num), self.den)
    #
    # "rich comparison" method
    def __lt__(self, other):
        """
        '<' operator
        """
        # supported type for operand except Rational
        if isinstance(other, int):
            return self.num - other * self.den < 0
        if not isinstance(other, Rational):
            return NotImplemented
        return self.num * other.den - other.num * self.den < 0
    #
    def __le__(self, other):
        """
        '<=' operator
        """
        # supported type for operand except Rational
        if isinstance(other, int):
            return self.num - other * self.den <= 0
        if not isinstance(other, Rational):
            return NotImplemented
        return self.num * other.den - other.num * self.den <= 0
    #
    def __eq__(self, other):
        """
        '==' operator
        """
        # supported type for operand except Rational
        if isinstance(other, int):
            return self.num - other * self.den == 0
        if not isinstance(other, Rational):
            return NotImplemented
        return self.num * other.den - other.num * self.den == 0
    #
    def __ne__(self, other):
        """
        '!=' or '<>' operator
        """
        # supported type for operand except Rational
        if isinstance(other, int):
            return self.num - other * self.den != 0
        if not isinstance(other, Rational):
            return NotImplemented
        return self.num * other.den - other.num * self.den != 0
    #
    def __gt__(self, other):
        """
        '>' operator
        """
        # supported type for operand except Rational
        if isinstance(other, int):
            return self.num - other * self.den > 0
        if not isinstance(other, Rational):
            return NotImplemented
        return self.num * other.den - other.num * self.den > 0
    #
    def __ge__(self, other):
        """
        '>=' operator
        """
        # supported type for operand except Rational
        if isinstance(other, int):
            return self.num - other * self.den >= 0
        if not isinstance(other, Rational):
            return NotImplemented
        return self.num * other.den - other.num * self.den >= 0
    #
    def __hash__(self):
        """
        calc hash value
        """
        return hash((self.num, self.den))
    #
    def __repr__(self):
        """
        'official' string representation
        """
        return '<Rational: num=%d, den=%d>' % (self.num, self.den)
    #
    def __str__(self):
        """
        'informal' string representation
        """
        ret = str(self.num)
        if self.den != 1:
            ret += '/' + str(self.den)
        return ret
    #
    def __bytes__(self):
        """
        'bytes()' operation
        """
        return bytes(str(self), 'utf8')
    #
    def __bool__(self):
        """
        'bool()' operation
        """
        return self.num != 0
    #
    def isinteger(self):
        """
        Does this Rational instance represent integer?
        """
        return self.den == 1
    #
    def num(self):
        """
        returns numerator of Rational
        """
        return self.num
    #
    def den(self):
        """
        returns denominator of Rational
        """
        return self.den
    #
    @staticmethod
    def parse(string):
        """
        parse string to Rational
        """
        posslash = string.find('/')
        if posslash < 0:
            return Rational(int(string), 1)
        else:
            strs = string.split('/')
            return Rational(int(strs[0].strip()), int(strs[1].strip()))
    #
    ZERO = None
    ONE = None

Rational.ZERO = Rational(0, 1)
Rational.ONE = Rational(1, 1)
