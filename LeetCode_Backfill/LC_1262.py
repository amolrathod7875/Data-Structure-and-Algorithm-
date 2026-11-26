class Solution(object):
    def maxSumDivThree(self, nums):
        dp = [0, float('-inf'), float('-inf')]

        for num in nums:
            ndp = dp[:]  # copy current bests
            for r in range(3):
                if dp[r] != float('-inf'):
                    new_r = (r + num) % 3
                    ndp[new_r] = max(ndp[new_r], dp[r] + num)
            dp = ndp

        # dp[0] holds the maximum sum divisible by 3
        return dp[0] if dp[0] != float('-inf') else 0