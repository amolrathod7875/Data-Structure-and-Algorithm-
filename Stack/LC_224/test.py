import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from code import Solution


class TestBasicCalculator(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.calculate("1 + 1"), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.calculate(" 2-1 + 2 "), 3)

    def test_example_3(self):
        self.assertEqual(self.solution.calculate("(1+(4+5+2)-3)+(6+8)"), 23)

    def test_single_number(self):
        self.assertEqual(self.solution.calculate("42"), 42)

    def test_simple_addition(self):
        self.assertEqual(self.solution.calculate("1+2+3"), 6)

    def test_simple_subtraction(self):
        self.assertEqual(self.solution.calculate("10-5-3"), 2)

    def test_nested_parentheses(self):
        self.assertEqual(self.solution.calculate("((1))"), 1)

    def test_multiple_nested(self):
        self.assertEqual(self.solution.calculate("((((1))))"), 1)

    def test_complex_expression(self):
        self.assertEqual(self.solution.calculate("1-(     -2)"), 3)

    def test_negative_inside_parentheses(self):
        self.assertEqual(self.solution.calculate("-(3+4)"), -7)

    def test_spaces_in_expression(self):
        self.assertEqual(self.solution.calculate(" 1 + 2 "), 3)
        self.assertEqual(self.solution.calculate(" 3 + 5 - 2 "), 6)

    def test_large_expression(self):
        self.assertEqual(self.solution.calculate("10+(5-(3+2))"), 10)

    def test_only_parentheses(self):
        self.assertEqual(self.solution.calculate("(1+(4+5+2)-3)"), 9)

    def test_chained_subtractions(self):
        self.assertEqual(self.solution.calculate("1-1+1"), 1)

    def test_nested_complex(self):
        self.assertEqual(self.solution.calculate("(1+(4+5+2)-3)+(6+8)"), 23)

    def test_double_negative(self):
        self.assertEqual(self.solution.calculate("1--1"), 2)

    def test_complex_with_spaces(self):
        self.assertEqual(self.solution.calculate("-(1+(4+5+2)-3)+(6+8)"), 5)


if __name__ == "__main__":
    unittest.main()
