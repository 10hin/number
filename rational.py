import sys

def gcd(a, b):
    """
    gratest common divisor
    """
    if a == 0 or b == 0:
        raise ArithmeticError('gcd of zero')
    p = a
    q = b
    if p < q:
        p = b
        q = a
    r = p % q
    while r != 0:
        p = q
        q = r
        r = p % q
    return q

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
            absNum = abs(num)
            absDen = abs(den)
            d = gcd(absNum, absDen)
            self._num = sign * absNum // d
            self._den = absDen // d
    
    def __add__(self, o):
        """
        '+' operator
        """
        # supported type for operand except Rational
        if isinstance(o, int):
            return Rational(self._num + self._den * o, self._den)
        if not instanceof(o, Rational):
            return NotImplemented
        return Rational(self._num * o._den + self._den * o._num, self._den * o._den)
    def __radd__(self, o):
        """
        fallback of '+' operator
        """
        if isinstance(o, int):
            return self.__add__(o)
        return NotImplemented
    
    def __sub__(self, o):
        """
        '-' binary operator
        """
        # supported type for operand except Rational
        if isinstance(o, int):
            return Rational(self._num - self._den * o, self._den)
        if not isinstance(o, Rational):
            return NotImplemented
        return Rational(self._num * o._den - self._den * o._num, self._den * o._den)
    def __rsub__(self, o):
        """
        fallback of '-' binary operator
        """
        if isinstance(o, int):
            return self.__neg__().__add__(- o)
        return NotImplemented
    
    def __mul__(self, o):
        """
        '*' operator
        """
        # supported type for operand except Rational
        if isinstance(o, int):
            return Rational(self._num * o, self._den)
        if not isinstance(o, Rational):
            return NotImplemented
        return Rational(self._num * o._num, self._den * o._den)
    def __rmul__(self, o):
        """
        fallback of '*' operator
        """
        return self.__mul__(o)
    
    def __truediv__(self, o):
        """
        '/' operator when '__future__.division' is in effect
        """
        # supported type for operand except Rational
        if isinstance(o, int):
            if o == 0:
                raise ZeroDivisionError('division by zero')
            return Rational(self._num, self._den * o)
        if not isinstance(o, Rational):
            return NotImplemented
        if o._num == 0:
            raise ZeroDivisionError('division by zero')
        return Rational(self._num * o._den, self._den * o._num)
    def __rtruediv__(self, o):
        """
        fallback of '/' operator when '__future__.division' is in effect
        """
        if isinstance(o, int):
            return Rational(self._den * o, self._num)
        return NotImplemented
    
    def __floordiv__(self, o):
        """
        '//' operator
        """
        return __truediv__(self, o)
    def __rfloordiv__(self, o):
        """
        fallback of '//' operator
        """
        return __rtruediv__(self, o)
    
    def __div__(self, o):
        """
        '/' operator
        """
        return __truediv__(self, o)
    def __rdiv__(self, o):
        """
        fallback of '/' operator
        """
        return __rtruediv__(self, o)
    
    def __mod__(self, o):
        """
        '%' operator
        """
        if isinstance(o, int):
            if o == 0:
                raise ZeroDivisionError('division by zero')
            return Rational(0, 1)
        if not isinstance(o, Rational):
            return NotImplemented
        if o._num == 0:
            raise eroDivisionError('division by zero')
        return Rational(0, 1)
    def __rmod__(self, o):
        """
        fallback of '%' operator
        """
        if self == Rational(0, 1):
            raise ZeroDivisionError('division by zero')
        return Rational(0, 1)
    
    def __divmod__(self, o):
        """
        'divmod()' operation
        """
        d = self.__floordiv__(o)
        m = self.__mod__(o)
        if d != NotImplemented and m != NotImplemented:
            return (d, m)
        return NotImplemented
    def __rdivmod__(self, o):
        """
        fallback of 'divmod()' operation
        """
        d = self.__rdiv__(o)
        m = self.__rmod__(o)
        if d != NotImplemented and m != NotImplemented:
            return (d, m)
        return NotImplemented
    
    def __pos__(self):
        """
        '+' unary operator
        """
        return self
    
    def __neg__(self):
        """
        '-' unary operator
        """
        return Rational(- self._num, self._den)
    
    def __abs__(self):
        """
        absolute value
        """
        return Rational(abs(self._num), self._den)
    
    # "rich comparison" method
    def __lt__(self, o):
        """
        '<' operator
        """
        # supported type for operand except Rational
        if isinstance(o, int):
            return self._num - o * self._den < 0
        if not isinstance(o, Rational):
            return NotImplemented
        return self._num * o._den - o._num * self._den < 0
    
    def __le__(self, o):
        """
        '<=' operator
        """
        # supported type for operand except Rational
        if isinstance(o, int):
            return self._num - o * self._den <= 0
        if not isinstance(o, Rational):
            return NotImplemented
        return self._num * o._den - o._num * self._den <= 0
    
    def __eq__(self, o):
        """
        '==' operator
        """
        # supported type for operand except Rational
        if isinstance(o, int):
            return self._num - o * self._den == 0
        if not isinstance(o, Rational):
            return NotImplemented
        return self._num * o._den - o._num * self._den == 0
    
    def __ne__(self, o):
        """
        '!=' or '<>' operator
        """
        # supported type for operand except Rational
        if isinstance(o, int):
            return self._num - o * self._den != 0
        if not isinstance(o, Rational):
            return NotImplemented
        return self._num * o._den - o._num * self._den != 0
    
    def __gt__(self, o):
        """
        '>' operator
        """
        # supported type for operand except Rational
        if isinstance(o, int):
            return self._num - o * self._den > 0
        if not isinstance(o, Rational):
            return NotImplemented
        return self._num * o._den - o._num * self._den > 0
    
    def __ge__(self, o):
        """
        '>=' operator
        """
        # supported type for operand except Rational
        if isinstance(o, int):
            return self._num - o * self._den >= 0
        if not isinstance(o, Rational):
            return NotImplemented
        return self._num * o._den - o._num * self._den >= 0
    
    def __cmp__(self, o):
        """
        fallback of comparing operator
        defined for Python2.X.
        """
        if sys.version_info.major == 2:
            if isinstance(o, int):
                return o * self._den - self._num
            if not isinstance(o, Rational):
                return NotImplemented
            return o._num * self._den - self._num * o._den
        else:
            return NotImplemented
    
    def __hash__(self):
        """
        calc hash value
        """
        return hash((self._num, self._den))
    
    def __unicode__(self):
        """
        'unicode()' operation
        defined for Python 2.X
        """
        if sys.version_info.major == 2:
            return unicode(self.__str__())
        else:
            return NotImplemented
    
    def __repr__(self):
        """
        'official' string representation
        """
        return '<Rational: num=%d, den=%d>' % (self._num, self._den)
    
    def __str__(self):
        """
        'informal' string representation
        """
        ret = str(self._num)
        if self._den != 1:
            ret += '/' + str(self._den)
        return ret
    
    def __bytes__(self):
        """
        'bytes()' operation
        """
        return bytes(str(self), 'utf8')
    
    def __bool__(self):
        """
        'bool()' operation
        """
        return self._num != 0
    
    def __nonzero__(self):
        """
        'bool()' operation
        defined for Python2.X
        """
        if sys.version_info.major == 2:
            return self.__bool__()
        else:
            return NotImplemented
    
    @staticmethod
    def parse(str):
        """
        parse string to Rational
        """
        posslash = str.find('/')
        if posslash < 0:
            return Rational(int(str), 1)
        else:
            strs = str.split('/')
            return Rational(int(strs[0].strip()), int(strs[1].strip()))

