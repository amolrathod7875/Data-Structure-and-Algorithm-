import unittest

from Math.LC_3360.code import Solution


class StoneRemovalTests(unittest.TestCase):
    def test_examples(self):
        self.assertIs(Solution().canAliceWin(12), True)
        self.assertIs(Solution().canAliceWin(1), False)

    def test_every_valid_input_against_cumulative_thresholds(self):
        thresholds = [sum(range(10, 10 - moves, -1))
                      for moves in range(1, 11)]
        for stones in range(1, 51):
            completed_moves = sum(total <= stones for total in thresholds)
            self.assertIs(Solution().canAliceWin(stones),
                          completed_moves % 2 == 1, stones)

    def test_turn_boundaries(self):
        for stones, expected in [(9, False), (10, True), (18, True),
                                 (19, False), (26, False), (27, True),
                                 (33, True), (34, False), (39, False),
                                 (40, True), (44, True), (45, False),
                                 (48, False), (49, True), (50, True)]:
            self.assertIs(Solution().canAliceWin(stones), expected, stones)


if __name__ == '__main__':
    unittest.main(verbosity=2)
