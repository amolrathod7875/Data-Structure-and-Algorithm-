class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        positive = nums[-1] * nums[-2] * nums[-3]

        negative = nums[0] * nums[1] * nums[-1]

        return max(positive, negative)
        