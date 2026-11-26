class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return sum((nums[i],nums[i+1]),nums[i+2])
        return 0
                
        