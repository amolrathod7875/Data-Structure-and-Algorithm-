class Solution:
    def elementsLessThanK(self, arr: list[int], k: int) -> list[int]:
        """Return a new list containing only the elements of `arr` that are strictly less than `k`."""
        return [x for x in arr if x < k]