import heapq

def KLargest(arr,k):
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
        if len(heap) > k :
            heapq.heappop(heap)
    return sorted(heap, reverse=True)

if __name__ == "__main__":
    nums = [1, 23, 12, 9, 30, 2, 50]
    print(KLargest(nums, 3))
