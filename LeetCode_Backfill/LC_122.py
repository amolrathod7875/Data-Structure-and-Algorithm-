class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        result = 0
        i = 0

        while i < n - 1:

            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            lmin = prices[i]

            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            lmax = prices[i]

            result += (lmax - lmin)

        return result