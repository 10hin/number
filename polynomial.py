"""
module polynomial
"""

from number import Number

def _ispolynomial(obj):
    if Number.isnumber(obj):
        return True
    if isinstance(obj, Polynomial):
        return True
    return False

class Polynomial(object):
    """
    regresenting polynomial
    """
    def __init__(self, coeffs):
        if not hasattr(coeffs, '__iter__'):
            raise TypeError('Polynomial(coeffs) constructor accepts iterable object only')
        maybe_coeffs = []
        for maybe_number in coeffs:
            if not Number.isnumber(maybe_number):
                raise TypeError('coeffs parameter contains something not to be number')
            maybe_coeffs.append(maybe_number)
        for cnt in reversed(maybe_coeffs):
            if cnt == 0 and 1 < len(maybe_coeffs):
                # remove last element(=0)
                del maybe_coeffs[len(maybe_coeffs) - 1]
            else:
                break
        self._coeffs = maybe_coeffs
    #
    def __pos__(self):
        """
        '+' unary operator
        """
        return self
    def __neg__(self):
        """
        '+' unary operator
        """
        new_coefs = list(self.coeffs())
        for cnt in range(0, self.dim):
            new_coefs[cnt] = -1 * new_coefs[cnt]
        return Polynomial(new_coefs)
    #
    def __add__(self, other):
        if not _ispolynomial(other):
            return NotImplemented
        if Number.isnumber(other):
            new_coefs = list(self.coeffs())
            new_coefs[0] = new_coefs[0] + other
        new_coefs = []
        may_new_dim = max(self.dim(), other.dim())
        for cnt in range(0, may_new_dim):
            self_coef = 0
            if cnt < self.dim():
                self_coef = self.coeff(cnt)
            other_coef = 0
            if cnt < other.dim():
                other_coef = other.coeff(cnt)
            new_coefs.append(self_coef + other_coef)
        for coef in reversed(new_coefs):
            if coef == 0 and 1 < len(new_coefs):
                # remove last element(=0)
                del new_coefs[len(new_coefs) - 1]
            else:
                break
        return Polynomial(new_coefs)
    #
    def deg(self):
        """
        returns degree of this Polynomial
        """
        return len(self._coeffs) - 1
    def dim(self):
        """
        returns dimension of this Polynomial
        """
        return len(self._coeffs)
    def coeff(self, deg):
        """
        returns cefficient of specified degree
        """
        return self._coeffs[deg]
    def coeffs(self):
        """
        returns tuple of coefficients
        """
        return tuple(self._coeffs)

