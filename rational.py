def gcd(a, b):
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
    def __init__(self, num, den):
        if den == 0:
            raise ZeroDivisionError('division by zero')
        if num * den < 0:
            sign = -1
        else:
            sign = 1
        d = gcd(abs(num), abs(den))
        self._num = sign * num // d
        self._den = den // d
    
    def __add__(self, o):
        return Rational(self._num * o._den + self._den * o._num, self._den * o._den)
    
    def __sub__(self, o):
        return Rational(self._num * o._den - self._den * o._num, self._den * o._den)
    
    def __mul__(self, o):
        return Rational(self._num * o._num, self._den * o._den)
    
    def __truediv__(self, o):
        if o._num == 0:
            raise ZeroDivisionError('division by zero')
        return Rational(self._num * o._den, self._den * o._num)
    
    def __floordiv__(self, o):
        if o._num == 0:
            raise ZeroDivisionError('divisioon by zero')
        return (self._num * o._den) // (self._den * o._num)
        
    
    @staticmethod
    def parse(str):
        posslash = str.find('/')
        if posslash < 0:
            return Rational(int(str), 1)
        else:
            strs = str.split('/')
            return Rational(int(strs[0].strip()), int(strs[1].strip()))
    
    def __repr__(self):
        return '<Rational: num=%d, den=%d>' % (self._num, self._den)
    
    def __str__(self):
        ret = str(self._num)
        if self._den != 1:
            ret += '/' + str(self._den)
        return ret
    
    def __bytes__(self):
        return str(self).encode('utf-8')
    
    def __bool__(self):
        return self._num != 0

