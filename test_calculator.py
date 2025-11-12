# GitHub Link: https://github.com/RyanL3248/lab10-RL-RL.git
#Partner 1: Ryan Linton
#Partner 2: Ryan Linton

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-3, -5), -8)
        self.assertEqual(add(-1, 3), 2)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5, 2), 3)
        self.assertEqual(sub(-4, -5), 1)
        self.assertEqual(sub(-5, 2), -7)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(1, 2), 2)
        self.assertEqual(mul(-1, 2), -2)
        self.assertEqual(mul(-3, -2), 6)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(1, 2), 2)
        self.assertEqual(div(-2, 4), -2)
        self.assertEqual(div(-3, -9), 3)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
        with self.assertRaises(AssertionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2, 8), 3)
        self.assertEqual(log(4, 16), 2)
        self.assertEqual(log(2, 2), 1)


    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
        with self.assertRaises(AssertionError):
            log(5, 0)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        with self.assertRaises(AssertionError):
            log(0, 5)


    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(0), 0)


    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()