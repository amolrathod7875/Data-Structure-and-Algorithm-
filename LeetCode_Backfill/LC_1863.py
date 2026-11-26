class Solution(object):
    def subsetXORSum(self, nums):
        total = 0
        n = len(nums)
        
        # Generate all 2^n subsets using bit manipulation
        for mask in range(1 << n):  # 0 to 2^n - 1
            xor_sum = 0
            for i in range(n):
                # If i-th bit is set in mask, include nums[i]
                if mask & (1 << i):
                    xor_sum ^= nums[i]
            total += xor_sum
        
        return total
        