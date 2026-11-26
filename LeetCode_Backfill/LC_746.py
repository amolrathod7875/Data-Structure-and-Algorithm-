class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        memo = [-1] * n
        def helper(index):
            if index > n-1:
                return 0
            if memo[index] != -1:
                return memo[index]
            
            onestep = cost[index] + helper(index + 1)
            twostep = cost[index] + helper(index + 2)

            memo[index] = min(onestep,twostep)

            return memo[index]
        return min(helper(0),helper(1))
        