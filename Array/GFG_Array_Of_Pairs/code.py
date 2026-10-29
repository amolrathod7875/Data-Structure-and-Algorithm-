class Solution:
    def arrayOfPairs(self, arr: list[int]) -> list[list[int]]:
        """Pair elements from both ends of the array, moving inward.

        For each step, pair the current leftmost element with the current
        rightmost element, then advance the left pointer and retreat the
        right pointer. When the array has an odd length, the middle element
        is paired with itself.
        """
        left = 0
        right = len(arr) - 1
        result = []
        while left <= right:
            result.append([arr[left], arr[right]])
            left += 1
            right -= 1
        return result