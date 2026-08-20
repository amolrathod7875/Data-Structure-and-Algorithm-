class Solution:
    def alternatingSum(self, nums: list[int]) -> int:
        total = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                total += num
            else:
                total -= num
        return total
