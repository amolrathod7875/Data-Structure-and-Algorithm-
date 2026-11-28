import unittest

from Array.LC_3947.code import Solution


class SaleTests(unittest.TestCase):
    def test_competing_boosted_and_regular_purchases(self):
        self.assertEqual(Solution().maximumSaleItems([[2, 5], [3, 3], [4, 6]], 9), 3)
        self.assertEqual(Solution().maximumSaleItems([[2, 5], [3, 3], [4, 6]], 8), 3)

    def test_equal_factors_are_distinct_types_with_a_bonus_limit(self):
        self.assertEqual(Solution().maximumSaleItems([[1, 2], [1, 3]], 10), 6)


if __name__ == "__main__":
    unittest.main()
