import unittest
from code import minCost


class TestMinCostToConnectRopes(unittest.TestCase):

    def test_gfg_example(self):
        ropes = [4, 3, 2, 6]
        self.assertEqual(minCost(ropes), 29)

    def test_five_ropes(self):
        ropes = [1, 2, 3, 4, 5]
        self.assertEqual(minCost(ropes), 33)

    def test_single_rope(self):
        ropes = [5]
        self.assertEqual(minCost(ropes), 0)

    def test_two_ropes(self):
        ropes = [2, 3]
        self.assertEqual(minCost(ropes), 5)

    def test_all_same(self):
        ropes = [4, 4, 4, 4]
        self.assertEqual(minCost(ropes), 32)

    def test_three_ropes(self):
        ropes = [1, 2, 3]
        self.assertEqual(minCost(ropes), 9)

    def test_already_sorted(self):
        ropes = [1, 10, 100]
        self.assertEqual(minCost(ropes), 122)

    def test_large_values(self):
        ropes = [8, 4, 6, 12, 14, 2, 10]
        self.assertEqual(minCost(ropes), 148)

    def test_does_not_mutate_input(self):
        ropes = [4, 3, 2, 6]
        minCost(ropes)
        self.assertEqual(ropes, [4, 3, 2, 6])


if __name__ == "__main__":
    unittest.main()
