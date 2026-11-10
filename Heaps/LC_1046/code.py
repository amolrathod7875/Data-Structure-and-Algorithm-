import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []
        for num in stones:
            heapq.heappush(heap, -num)
        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if y != x:
                heapq.heappush(heap, -(y - x))
        return -heap[0] if heap else 0