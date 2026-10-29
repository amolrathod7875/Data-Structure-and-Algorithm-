class Solution:
    def pushZerosToEnd(self, arr: list[int]) -> None:
        """Move all zeros to the end of the array in place, preserving the
        relative order of the non-zero elements, using two pointers.

        `j` tracks the position where the next non-zero element should be
        placed. `i` scans the array; whenever a non-zero is found it is
        swapped into position `j` and `j` advances.
        """
        j = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        return arr