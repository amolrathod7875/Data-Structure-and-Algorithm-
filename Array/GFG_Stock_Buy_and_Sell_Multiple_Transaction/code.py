class Solution:
    def maxProfit(self, prices):
        total_profit = 0 
        n = len(prices)
        for i in range(1, n) :
            price_diff = prices[i] - prices[i-1]
            if price_diff > 0 :
                total_profit += price_diff
        return total_profit
