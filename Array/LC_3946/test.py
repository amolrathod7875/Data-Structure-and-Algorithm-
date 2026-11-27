from itertools import product
import random
import unittest

from Array.LC_3946.code import Solution


def oracle(items, budget):
    best = 0
    for counts in product(*(range(budget // price + 1) for _, price in items)):
        if sum(count * item[1] for count, item in zip(counts, items)) > budget:
            continue
        free = sum(1 for i, count in enumerate(counts) if count
                   for j in range(len(items))
                   if i != j and items[j][0] % items[i][0] == 0)
        best = max(best, sum(counts) + free)
    return best


class SaleTests(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().maximumSaleItems([[6, 2], [2, 6], [3, 4]], 9), 4)
        self.assertEqual(Solution().maximumSaleItems(
            [[2, 4], [3, 2], [4, 1], [6, 4], [12, 4]], 8), 10)

    def test_bonus_boundaries(self):
        for items, budget, expected in [
            ([[1, 2]], 5, 2), ([[1, 10]], 9, 0),
            ([[2, 1], [2, 1]], 3, 5),
            ([[2, 1], [4, 10], [8, 10]], 3, 5),
            ([[2, 2], [3, 2]], 4, 2),
            ([[1, 1]] * 1000, 1500, 1000500),
        ]:
            self.assertEqual(Solution().maximumSaleItems(items, budget), expected)

    def test_random_copy_enumeration(self):
        rng = random.Random(3946)
        for _ in range(400):
            items = [[rng.randint(1, 12), rng.randint(1, 6)]
                     for _ in range(rng.randint(1, 4))]
            budget = rng.randint(1, 9)
            original = [item[:] for item in items]
            self.assertEqual(Solution().maximumSaleItems(items, budget), oracle(items, budget))
            self.assertEqual(items, original)


if __name__ == '__main__':
    unittest.main(verbosity=2)
