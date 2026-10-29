class Solution:
    def reverseArray(self, arr: list[int]) -> list[int]:
        """Reverse the array in place using two pointers.

        Swaps elements from both ends, moving toward the center, until
        the pointers meet.
        """
        left = 0
        right = len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr