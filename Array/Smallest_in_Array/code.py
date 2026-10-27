class Solution:
    def findMin(self, arr: list[int]) -> int:
        """Return the smallest element in the array.

        Scans every element once, keeping track of the minimum seen so far.
        """
        if not arr:
            raise ValueError("Array must not be empty")

        min_ = float("inf")

        for num in arr:
            if num < min_:
                min_ = num
        return min_