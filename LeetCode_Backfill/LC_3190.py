class Solution(object):
    def minimumOperations(self, nums):
        count = 0
        for i in range(len(nums)):
            divisible = nums[i] % 3
            if divisible != 0:
                count += 1
        return count
        