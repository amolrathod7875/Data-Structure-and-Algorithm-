class Solution(object):
    def maxProfit(self, prices):
        j = 0
        profit = 0
        for i in range(1,len(prices)):
            if prices[j] > prices[i]:
                j = i
            else:
                profit = max(profit,prices[i] - prices[j])
        return profit
        