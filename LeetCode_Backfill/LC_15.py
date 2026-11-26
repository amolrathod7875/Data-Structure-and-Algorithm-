class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                left = i+1
                right = len(nums) - 1
                while left < right:
                    sumThree = nums[i] + nums[left] + nums[right]
                    if sumThree == 0:
                        res.append([nums[i],nums[left],nums[right]])
                        left += 1
                        while left<right and nums[left] == nums[left-1]:
                            left += 1
                    elif sumThree < 0:
                        left += 1
                    else:
                        right -= 1
        return res