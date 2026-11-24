from math import gcd, lcm
from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        best = 0
        for left in range(len(nums)):
            product, common_gcd, common_lcm = 1, 0, 1
            for right in range(left, len(nums)):
                value = nums[right]
                product *= value
                common_gcd = gcd(common_gcd, value)
                common_lcm = lcm(common_lcm, value)
                if product == common_gcd * common_lcm:
                    best = max(best, right - left + 1)
        return best
