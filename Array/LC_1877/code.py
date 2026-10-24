class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        """Minimize the maximum pair sum by pairing the smallest with the largest.

        After sorting, the optimal pairing is (nums[0], nums[n-1]),
        (nums[1], nums[n-2]), ... . The answer is the largest of these
        pair sums.
        """
        n = len(nums)
        if n == 0:
            return 0

        nums.sort()
        result = []
        left = 0
        right = n - 1
        while left < right:
            result.append(nums[left] + nums[right])
            left += 1
            right -= 1
        return max(result) if result else 0