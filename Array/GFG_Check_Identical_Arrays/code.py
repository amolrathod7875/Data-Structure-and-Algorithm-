class Solution:
    def checkIdentical(self, a: list[int], b: list[int]) -> bool:
        """Return True if arrays `a` and `b` have the same length and the same
        elements in the same order; otherwise return False.
        """
        if len(a) != len(b):
            return False

        for x, y in zip(a, b):
            if x != y:
                return False
        return True