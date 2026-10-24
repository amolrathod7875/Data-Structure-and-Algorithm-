class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """Move all zeros to the end of the array in place, preserving the
        relative order of the non-zero elements.
        """
        result = []

        for num in nums:
            if num != 0:
                result.append(num)

        if len(result) != len(nums):
            zeros_needed = len(nums) - len(result)
            zeros = [0] * zeros_needed
            result.extend(zeros)

        nums[:] = result