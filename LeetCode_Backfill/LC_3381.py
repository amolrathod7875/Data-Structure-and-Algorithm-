class Solution(object):
    def maxSubarraySum(self, nums, k):
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        # min_prefix_sum[r] will store the minimum prefix sum
        # found so far for an index i where i % k == r.
        min_prefix_sum = {}
        max_sum = float('-inf')

        for j in range(n + 1):
            rem = j % k

            # If we have seen this remainder before, it means we can form a
            # subarray of length divisible by k.
            if rem in min_prefix_sum:
                # The subarray sum is the current prefix sum minus the minimum
                # prefix sum seen for the same remainder.
                current_sum = prefix_sum[j] - min_prefix_sum[rem]
                max_sum = max(max_sum, current_sum)

            # Update the minimum prefix sum for the current remainder.
            min_prefix_sum[rem] = min(min_prefix_sum.get(rem, float('inf')), prefix_sum[j])
        
        return max_sum if max_sum != float('-inf') else 0