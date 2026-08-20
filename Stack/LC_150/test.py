import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from code import Solution


class TestEvaluateReversePolishNotation(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.evalRPN(["2", "1", "+", "3", "*"]), 9)

    def test_example_2(self):
        self.assertEqual(self.solution.evalRPN(["4", "13", "5", "/", "+"]), 6)

    def test_example_3(self):
        self.assertEqual(self.solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)

    def test_single_number(self):
        self.assertEqual(self.solution.evalRPN(["42"]), 42)

    def test_negative_number(self):
        self.assertEqual(self.solution.evalRPN(["-2", "3", "*"]), -6)

    def test_division_truncate_toward_zero(self):
        self.assertEqual(self.solution.evalRPN(["-2", "3", "/"]), 0)

    def test_multiplication(self):
        self.assertEqual(self.solution.evalRPN(["3", "4", "*"]), 12)

    def test_subtraction(self):
        self.assertEqual(self.solution.evalRPN(["10", "3", "-"]), 7)

    def test_chained_operations(self):
        self.assertEqual(self.solution.evalRPN(["1", "2", "+", "3", "4", "+", "*"]), 21)

    def test_all_operators(self):
        self.assertEqual(self.solution.evalRPN(["5", "3", "2", "*", "+"]), 11)

    def test_complex_expression(self):
        self.assertEqual(self.solution.evalRPN(["4", "2", "3", "*", "+"]), 10)

    def test_division_positive(self):
        self.assertEqual(self.solution.evalRPN(["8", "3", "/"]), 2)

    def test_large_numbers(self):
        self.assertEqual(self.solution.evalRPN(["100", "200", "+", "2", "/", "5", "*"]), 750)

    def test_zero_operands(self):
        self.assertEqual(self.solution.evalRPN(["0", "1", "+"]), 1)
        self.assertEqual(self.solution.evalRPN(["0", "5", "*"]), 0)


if __name__ == "__main__":
    unittest.main()
