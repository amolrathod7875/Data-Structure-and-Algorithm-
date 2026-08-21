import heapq

def sortNearlySorted(arr, k):
    n = len(arr)
    heap = arr[:k+1]
    heapq.heapify(heap)

    result = []
    idx = k + 1 
    for i in range(n):
        result.append(heapq.heappop(heap))
        if idx < n :
            heapq.heappush(heap, arr[idx])
            idx += 1 
    return result
