class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        j = 0
        count = 0
        for i in range(len(nums)):
            while nums[i] - nums[j] > 1:
                j += 1
            if nums[i] - nums[j] == 1:
                count = max(count,i-j+1)
        return count