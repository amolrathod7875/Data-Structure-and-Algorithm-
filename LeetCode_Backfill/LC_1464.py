class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)- 1 ):
            j = i + 1 
            if ((nums[i] - 1) * (nums[j] - 1)) > 0 :
                result = max(result, ((nums[i] - 1) * (nums[j] - 1)))

        return result