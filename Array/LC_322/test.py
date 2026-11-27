from collections import deque
import random
import unittest

from Array.LC_322.code import Solution


def bfs(coins, amount):
    queue = deque([(0, 0)])
    seen = {0}
    while queue:
        total, count = queue.popleft()
        if total == amount:
            return count
        for coin in coins:
            next_total = total + coin
            if next_total <= amount and next_total not in seen:
                seen.add(next_total)
                queue.append((next_total, count + 1))
    return -1


class CoinTests(unittest.TestCase):
    def test_examples_and_greedy_failure(self):
        for coins, amount, expected in [([1, 2, 5], 11, 3), ([2], 3, -1),
                                        ([1], 0, 0), ([1, 3, 4], 6, 2),
                                        ([2147483647], 10000, -1),
                                        ([1], 10000, 10000)]:
            self.assertEqual(Solution().coinChange(coins, amount), expected)

    def test_random_breadth_first_search(self):
        rng = random.Random(322)
        for _ in range(1000):
            coins = rng.sample(range(1, 20), rng.randint(1, 8))
            amount = rng.randint(0, 80)
            self.assertEqual(Solution().coinChange(coins, amount), bfs(coins, amount))


if __name__ == '__main__':
    unittest.main(verbosity=2)
