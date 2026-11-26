from math import isqrt


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        squares = [root * root for root in range(1, isqrt(n) + 1)]
        winning = bytearray(n + 1)
        for stones in range(1, n + 1):
            for square in squares:
                if square > stones:
                    break
                if not winning[stones - square]:
                    winning[stones] = 1
                    break
        return bool(winning[n])
