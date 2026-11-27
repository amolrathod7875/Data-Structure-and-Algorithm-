from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        limit = max(factor for factor, _ in items)
        frequencies = [0] * (limit + 1)
        for factor, _ in items:
            frequencies[factor] += 1
        gains = [0] * (limit + 1)
        for factor in range(1, limit + 1):
            gains[factor] = sum(frequencies[multiple]
                                for multiple in range(factor, limit + 1, factor))

        dp = [0] * (budget + 1)
        for factor, price in items:
            for capacity in range(budget, price - 1, -1):
                dp[capacity] = max(dp[capacity], dp[capacity - price] + gains[factor])
            for capacity in range(price, budget + 1):
                dp[capacity] = max(dp[capacity], dp[capacity - price] + 1)
        return dp[budget]
