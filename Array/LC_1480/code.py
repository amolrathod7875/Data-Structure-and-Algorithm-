class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        i = 0 
        sum = 0 
        result = []
        while i < len(nums):
            sum += nums[i]
            result.append(sum)
            i += 1
        return result 
