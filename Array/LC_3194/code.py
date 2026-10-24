class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        """Return the minimum average of any pair formed by the smallest and
        largest remaining elements after sorting.

        The optimal pairing strategy is to pair the smallest element with the
        largest, the second smallest with the second largest, and so on. The
        minimum of those pair averages is the answer.
        """
        n = len(nums)
        if n == 0:
            return 0.0

        nums.sort()
        ans = float("inf")
        left = 0
        right = n - 1
        while left < right:
            avg = (nums[left] + nums[right]) / 2
            ans = min(ans, avg)
            left += 1
            right -= 1
        return ans