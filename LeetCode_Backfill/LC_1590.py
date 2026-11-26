class Solution(object):
    def minSubarray(self, nums, p):
        n = len(nums)
        target_rem = sum(nums) % p
        if target_rem == 0:
            return 0
            
        # A map to store the last seen index of a prefix sum remainder.
        # We initialize with {0: -1} to handle cases where the subarray
        # to be removed starts from index 0.
        rem_map = {0: -1}
        min_len = n  # Initialize with a value larger than any possible answer.
        current_sum = 0
        
        for j in range(n):
            current_sum += nums[j]
            current_rem = current_sum % p
            
            # We need to find a prefix sum `rem_map[i]` such that (current_rem - rem_map[i]) % p == target_rem.
            # This means rem_map[i] should be (current_rem - target_rem) % p.
            needed_rem = (current_rem - target_rem + p) % p
            if needed_rem in rem_map:
                min_len = min(min_len, j - rem_map[needed_rem])
            
            rem_map[current_rem] = j
            
        # If min_len is still n, it means the only solution is to remove the whole array,
        # which is not allowed. Or no solution was found.
        return min_len if min_len < n else -1
        