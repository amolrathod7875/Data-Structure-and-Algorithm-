import unittest

from Array.LC_2279.code import Solution


class BagTests(unittest.TestCase):
    def test_already_full_and_cheapest_deficit_first(self):
        self.assertEqual(Solution().maximumBags([7, 4, 5, 3], [1, 4, 3, 2], 3), 3)

    def test_no_bag_can_be_filled(self):
        self.assertEqual(Solution().maximumBags([4, 5], [0, 1], 3), 0)


if __name__ == "__main__":
    unittest.main()
