from math import gcd


class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        max_strength = 0

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] * nums[j] <= max_strength:
                    break
                g = gcd(nums[i], nums[j])
                strength = (nums[i] * nums[j]) // (g * g)
                if strength > max_strength:
                    max_strength = strength

        return max_strength
