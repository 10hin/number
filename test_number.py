from number import Number
from rational import Rational
import unittest

class NumberTest(unittest.TestCase):
    def test_isnumber_integerLiteral(self):
        self.assertTrue(Number.isnumber(0))
        self.assertTrue(Number.isnumber(1))
        self.assertTrue(Number.isnumber(2))
        self.assertTrue(Number.isnumber(3))
        self.assertTrue(Number.isnumber(4))
        self.assertTrue(Number.isnumber(5))
        self.assertTrue(Number.isnumber(6))
        self.assertTrue(Number.isnumber(7))
        self.assertTrue(Number.isnumber(8))
        self.assertTrue(Number.isnumber(9))
        self.assertTrue(Number.isnumber(-1))
    def test_isnumber_floatLiteral(self):
        self.assertTrue(Number.isnumber(1.5))
        self.assertTrue(Number.isnumber(-2.3))
    def test_isnumber_Rational(self):
        self.assertTrue(Number.isnumber(Rational(1, 2)))
        self.assertTrue(Number.isnumber(Rational.parse('-2/3')))
    def test_isnumber_notInteger(self):
        self.assertFalse(Number.isnumber('10'))

if __name__ == '__main__':
    unittest.main()

