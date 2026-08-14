import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from code import Solution


class TestBasicCalculatorII(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.calculate("3+2*2"), 7)

    def test_example_2(self):
        self.assertEqual(self.solution.calculate(" 3/2 "), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.calculate(" 3+5 / 2 "), 5)

    def test_single_number(self):
        self.assertEqual(self.solution.calculate("42"), 42)

    def test_addition_only(self):
        self.assertEqual(self.solution.calculate("1+2+3"), 6)

    def test_subtraction_only(self):
        self.assertEqual(self.solution.calculate("10-5-2"), 3)

    def test_multiplication_only(self):
        self.assertEqual(self.solution.calculate("2*3*4"), 24)

    def test_division_only(self):
        self.assertEqual(self.solution.calculate("10/2/2"), 2)

    def test_mixed_operators(self):
        self.assertEqual(self.solution.calculate("1-1+1"), 1)

    def test_multiplication_before_addition(self):
        self.assertEqual(self.solution.calculate("2+3*4"), 14)

    def test_division_truncate_toward_zero(self):
        self.assertEqual(self.solution.calculate("14-3/4"), 14)

    def test_negative_result(self):
        self.assertEqual(self.solution.calculate("1-2*3"), -5)

    def test_spaces_in_expression(self):
        self.assertEqual(self.solution.calculate(" 3 + 2 * 2 "), 7)

    def test_large_numbers(self):
        self.assertEqual(self.solution.calculate("100000/200/10"), 50)

    def test_zero_in_expression(self):
        self.assertEqual(self.solution.calculate("0*0"), 0)
        self.assertEqual(self.solution.calculate("0+0"), 0)

    def test_division_positive(self):
        self.assertEqual(self.solution.calculate("9/3"), 3)

    def test_division_negative(self):
        self.assertEqual(self.solution.calculate("-3/2"), -1)


if __name__ == "__main__":
    unittest.main()
