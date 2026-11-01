class Solution:
    def maxProfit(self, prices):
        j = 0 
        n = len(prices)
        profit = 0 
        for i in range(1, n):
            if prices[j] > prices[i] : 
                j = i 
            else:
                profit = max(profit, (prices[i] - prices[j]))
        return profit
