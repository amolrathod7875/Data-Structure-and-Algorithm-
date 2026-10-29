class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        """Apply operations to the array and shift zeros to the end.

        First pass: for each adjacent pair (i, i+1), if equal, double
        nums[i] and set nums[i+1] to 0.

        Second pass (two pointers): move all non-zero elements to the
        front, preserving relative order, and zeros to the end.
        """
        n = len(nums)

        # Pass 1: apply operations on adjacent equal pairs
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        # Pass 2: move zeros to the end (two pointers, in place)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return nums