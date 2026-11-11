import heapq

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        heap = []
        for row in matrix:
            for num in row:
                heapq.heappush(heap, num)

        for i in range(k):
            ans = heapq.heappop(heap)
        return ans