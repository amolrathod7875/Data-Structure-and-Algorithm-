class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        lookup = set(nums)
        mn = min(nums)
        mx = max(nums)
        result = []

        for x in range(mn + 1, mx):
            if x not in lookup:
                result.append(x)

        return result
