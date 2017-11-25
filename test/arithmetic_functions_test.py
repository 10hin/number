import unittest
import arithmetic_functions as math

class GcdTests(unittest.TestCase):
    def gcdOfZero1():
        unittest.assertRaises(ArithmeticError, math.gcd, 0, 2)

if __name__ == ‘__main__’:
    unittest.main()
