class Solution:
    def smallestRangeII(self, nums: list[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = nums[n - 1 ] - nums[0]
        for i in range(1, n) :
            minH = min(nums[i] - k, nums[0] + k )
            maxH = max(nums[i - 1] + k , nums[n - 1 ] - k)
            res = min(res, (maxH - minH))
        return res
