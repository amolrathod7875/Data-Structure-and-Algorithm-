import heapq

def minCost(ropes):
    # Edge case: 0 or 1 rope needs no connections
    if len(ropes) <= 1:
        return 0

    # Work on a copy so the input list is not mutated
    heap = ropes[:]
    heapq.heapify(heap)          # O(n) build min-heap

    total = 0
    # Keep combining the two shortest ropes until one remains
    while len(heap) > 1:
        a = heapq.heappop(heap)  # shortest
        b = heapq.heappop(heap)  # second shortest
        cost = a + b             # cost to connect them
        total += cost
        heapq.heappush(heap, cost)  # new combined rope back into heap

    return total


if __name__ == "__main__":
    ropes = [4, 3, 2, 6]
    print(minCost(ropes))   # 29
