import unittest
import arithmetic_functions as math

class GcdTests(unittest.TestCase):
    def test_gcd_of_zero1(self):
        self.assertRaises(ArithmeticError, math.gcd, 0, 2)
    def test_gcd_of_zero2(self):
        self.assertRaises(ArithmeticError, math.gcd, 2, 0)
    def test_gcd_of_zero3(self):
        self.assertRaises(ArithmeticError, math.gcd, 0, 0)
    def test_gcd_of_positives(self):
        for (p2, p3, p5) in self.gen_factor():
            for (q2, q3, q5) in self.gen_factor():
                expected = (2 ** min(p2, q2)) * (3 ** min(p3, q3)) * (5 ** min(p5, q5))
                arg_a = (2 ** p2) * (3 ** p3) * (5 ** p5)
                arg_b = (2 ** q2) * (3 ** q3) * (5 ** q5)
                self.assertEqual(expected, math.gcd(arg_a, arg_b))
    def test_gcd_of_negatives(self):
        for (p2, p3, p5) in self.gen_factor():
            for (q2, q3, q5) in self.gen_factor():
                expected = (2 ** min(p2, q2)) * (3 ** min(p3, q3)) * (5 ** min(p5, q5))
                arg_a = -1 * (2 ** p2) * (3 ** p3) * (5 ** p5)
                arg_b = -1 * (2 ** q2) * (3 ** q3) * (5 ** q5)
                self.assertEqual(expected, math.gcd(arg_a, arg_b))
    def test_gcd_of_positive_negative(self):
        for (p2, p3, p5) in self.gen_factor():
            for (q2, q3, q5) in self.gen_factor():
                expected = (2 ** min(p2, q2)) * (3 ** min(p3, q3)) * (5 ** min(p5, q5))
                arg_a = (2 ** p2) * (3 ** p3) * (5 ** p5)
                arg_b = -1 * (2 ** q2) * (3 ** q3) * (5 ** q5)
                self.assertEqual(expected, math.gcd(arg_a, arg_b))
    def test_gcd_of_negative_positive(self):
        for (p2, p3, p5) in self.gen_factor():
            for (q2, q3, q5) in self.gen_factor():
                expected = (2 ** min(p2, q2)) * (3 ** min(p3, q3)) * (5 ** min(p5, q5))
                arg_a = -1 * (2 ** p2) * (3 ** p3) * (5 ** p5)
                arg_b = (2 ** q2) * (3 ** q3) * (5 ** q5)
                self.assertEqual(expected, math.gcd(arg_a, arg_b))
    def gen_factor(self):
        res = []
        for i in (0, 1, 2):
            for j in (0, 1, 2):
                for k in (0, 1, 2):
                    res.append((i, j, k))
        return res

if __name__ == '__main__':
    unittest.main()
