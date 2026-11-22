import itertools
import unittest

from String.LC_2124.code import Solution


class CheckStringTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        for value, expected in [("aaabbb", True), ("abab", False), ("bbb", True)]:
            with self.subTest(value=value):
                self.assertEqual(self.solution.checkString(value), expected)

    def test_single_characters_and_homogeneous_strings(self):
        for value in ["a", "b", "aaa", "bbbb"]:
            self.assertTrue(self.solution.checkString(value))

    def test_boundaries_and_late_violation(self):
        self.assertTrue(self.solution.checkString("a" * 50 + "b" * 50))
        self.assertFalse(self.solution.checkString("a" * 98 + "ba"))
        self.assertFalse(self.solution.checkString("ba"))

    def test_exhaustive_short_strings(self):
        for length in range(1, 11):
            for letters in itertools.product("ab", repeat=length):
                value = "".join(letters)
                self.assertEqual(
                    self.solution.checkString(value),
                    value == "".join(sorted(value)),
                    value,
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
