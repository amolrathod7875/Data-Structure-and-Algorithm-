class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        audit = set(nums)
        result = []
        for missing in range(1, len(nums) + 1 ):
            if missing not in audit:
                result.append(missing)
        return result