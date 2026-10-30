class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)

        if n <= 1:
            return

        k = k % n

        def reverse_range(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse_range(0, n - 1)
        reverse_range(0, k - 1)
        reverse_range(k, n - 1)
