import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from code import Solution


class TestValidParentheses(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()

    def test_simple_valid(self):
        self.assertTrue(self.solution.isValid("()"))

    def test_simple_invalid(self):
        self.assertFalse(self.solution.isValid("(]"))

    def test_all_bracket_types_valid(self):
        self.assertTrue(self.solution.isValid("()[]{}"))

    def test_all_bracket_types_invalid(self):
        self.assertFalse(self.solution.isValid("([)]"))

    def test_nested_valid(self):
        self.assertTrue(self.solution.isValid("{[]}"))

    def test_nested_invalid(self):
        self.assertFalse(self.solution.isValid("([)]"))

    def test_opening_only(self):
        self.assertFalse(self.solution.isValid("([{"))

    def test_closing_only(self):
        self.assertFalse(self.solution.isValid(")]}"))

    def test_empty_string(self):
        self.assertTrue(self.solution.isValid(""))

    def test_single_bracket(self):
        self.assertFalse(self.solution.isValid("("))
        self.assertFalse(self.solution.isValid(")"))

    def test_mismatched_nested(self):
        self.assertFalse(self.solution.isValid("([)]"))

    def test_complex_valid(self):
        self.assertTrue(self.solution.isValid("({[]})"))

    def test_complex_invalid(self):
        self.assertFalse(self.solution.isValid("([)]"))

    def test_multiple_same_type(self):
        self.assertTrue(self.solution.isValid("((()))"))
        self.assertTrue(self.solution.isValid("(([]))"))
        self.assertFalse(self.solution.isValid("(([])"))

    def test_extra_closing(self):
        self.assertFalse(self.solution.isValid("())"))
        self.assertFalse(self.solution.isValid("())[]{}"))

    def test_extra_opening(self):
        self.assertFalse(self.solution.isValid("(()"))
        self.assertFalse(self.solution.isValid("(()[]{}"))


if __name__ == "__main__":
    unittest.main()
