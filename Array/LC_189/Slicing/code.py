class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """Rotate the array to the right by `k` steps using slicing.

        Builds a new list from the last `k` elements followed by the
        first `n - k` elements, then writes it back into `nums` in place
        via slice assignment.
        """
        n = len(nums)

        if n == 0:
            return

        k = k % n

        if k == 0:
            return

        nums[:] = nums[-k:] + nums[:-k]