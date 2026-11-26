from functools import lru_cache
from math import isqrt
import unittest

from Math.LC_1510.code import Solution


@lru_cache(None)
def minimax(stones):
    return any(not minimax(stones - root * root)
               for root in range(1, isqrt(stones) + 1))


def forward_oracle(limit):
    """Mark all positions that can move into each finalized losing position."""
    winning = bytearray(limit + 1)
    for losing in range(limit + 1):
        if not winning[losing]:
            for root in range(1, isqrt(limit - losing) + 1):
                winning[losing + root * root] = 1
    return winning


class SquareGameTests(unittest.TestCase):
    def test_examples_and_losing_positions(self):
        for stones, expected in [(1, True), (2, False), (4, True),
                                 (7, False), (17, False)]:
            self.assertIs(Solution().winnerSquareGame(stones), expected)

    def test_small_positions_against_recursive_minimax(self):
        for stones in range(1, 201):
            self.assertIs(Solution().winnerSquareGame(stones), minimax(stones), stones)

    def test_perfect_squares_win_immediately(self):
        for root in [1, 2, 3, 10, 31, 100, 316]:
            self.assertIs(Solution().winnerSquareGame(root * root), True)

    def test_large_boundaries_against_forward_propagation(self):
        oracle = forward_oracle(100000)
        for stones in [99990, 99999, 100000]:
            self.assertIs(Solution().winnerSquareGame(stones),
                          bool(oracle[stones]), stones)


if __name__ == '__main__':
    unittest.main(verbosity=2)
