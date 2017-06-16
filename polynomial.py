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
def _remove_zero_coeff(coeffs):
    """
    リスト末尾の値が0のエントリを削除したリストを返す
    ただしすべての要素が0の時は0が１つだけ含まれるリストを返す
    """
    result = coeffs[:]
    for elm in reversed(coeffs):
        if elm == 0 and 1 < len(result):
            # remove last element
            del result[len(result) - 1]
        else:
            break
    return result
def _check_coeff_list(maybe_coeffs):
    """
    引数が数値を要素とするiterableかどうかを判定する
    数値のみからなる場合はtrueを、
    数値以外を含む場合はfalseを返す。
    数値かどうかの判定にはNumber.isnumber()を用いる
    """
    for elm in maybe_coeffs:
        if not Number.isnumber(elm):
            return false
    return true

class Polynomial(object):
    """
    regresenting polynomial
    """
    def __init__(self, coeffs):
        if not _check_coeff_list(coeffs):
            raise TypeError('Polynomial(coeffs) constructor accept iterable of number')
        self._coeffs = _remove_zero_coeff(coeffs)
    #
    def __pos__(self):
        """
        '+' unary operator
        """
        return self
    def __neg__(self):
        """
        '-' unary operator
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
        new_coefs = _remove_zero_coeff(new_coefs):
        return Polynomial(new_coefs)
    def __radd__(self, other):
        return self.__add__(other)
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

