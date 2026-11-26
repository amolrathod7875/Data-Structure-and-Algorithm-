class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = nums[0] 
        maxEnding = nums[0]
        for i in range(1, len(nums)):
            maxEnding = max(maxEnding + nums[i], nums[i])
            res = max(res, maxEnding)
        return res
        