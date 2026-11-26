class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        audit = set(nums)
        missing = 1

        while missing in audit:
            missing += 1

        return missing
