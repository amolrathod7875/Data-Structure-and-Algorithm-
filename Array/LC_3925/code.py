class Solution:
    def concatenateArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * (2 * n)

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[n - 1 - i]

        return ans
