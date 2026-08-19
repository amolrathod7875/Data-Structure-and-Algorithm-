from typing import List

class Solution:

    def max_heapify(arr, heap_size, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < heap_size and arr[left] > arr[largest]:
            largest = left

        if right < heap_size and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            Solution.max_heapify(arr, heap_size, largest)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            Solution.max_heapify(nums, n, i)

        heap_size = n

        # Remove maximum k-1 times
        for _ in range(k - 1):
            nums[0], nums[heap_size - 1] = nums[heap_size - 1], nums[0]
            heap_size -= 1
            Solution.max_heapify(nums, heap_size, 0)

        return nums[0]
