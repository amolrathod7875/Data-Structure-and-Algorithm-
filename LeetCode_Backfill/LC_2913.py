class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        Sum = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums) + 1):
                subarray = nums[i:j]
                Sum = Sum + len(set(subarray)) * len(set(subarray))
        return Sum 
        