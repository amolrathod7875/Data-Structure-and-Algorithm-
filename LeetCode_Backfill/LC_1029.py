class Solution(object):
    def twoCitySchedCost(self, costs):
        costs.sort(key=lambda x : x[0] - x[1])
        n = len(costs)
        total_cost = 0
        for i in range(n//2):
            total_cost += costs[i][0]
        for i in range(n//2,n):
            total_cost += costs[i][1]

        return total_cost        