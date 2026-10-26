class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """Return the k-th largest element in the array.

        Sorts the array in ascending order and picks the element `k`
        positions from the end, i.e. `nums[-k]`.
        """
        nums.sort()
        return nums[-k]