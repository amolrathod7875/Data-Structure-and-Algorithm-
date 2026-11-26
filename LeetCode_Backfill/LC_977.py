class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        for i in range(n):
            res[i] = nums[i] ** 2
        res.sort()
        return res