class Solution:
    def getSmaller(self, arr, target):
        """Return a new list containing only the elements of `arr` that are strictly less than `target`."""
        return [x for x in arr if x < target]