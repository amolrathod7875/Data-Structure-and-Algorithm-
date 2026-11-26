
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        result = 0
        maximum = max(nums)

        for num in nums:
            result += maximum - num

        return result
