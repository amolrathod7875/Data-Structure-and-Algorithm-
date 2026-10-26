class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """Find the single missing number in the range [0, n].

        Uses the arithmetic series sum formula: the sum of 0..n is
        n*(n+1)/2. Subtracting the sum of the given array from this
        total yields the missing number.
        """
        n = len(nums)
        total_sum = (n * (n + 1)) // 2
        nums_sum = sum(nums)
        return total_sum - nums_sum