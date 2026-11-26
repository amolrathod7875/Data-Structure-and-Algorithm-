class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        freq = Counter(nums)

        left = 0
        right = len(nums)
        ans = 0

        for cnt in freq.values():
            right -= cnt
            ans += left * cnt * right
            left += cnt

        return ans
        