# GFG K Largest Elements (Heap)

## Problem Statement

Given an array `arr` and an integer `k`, return the **k largest elements** of the array.

This is the **heap-based** solution to the same problem solved earlier with plain sorting (see `Array/k largest elements in an array`). Here we use a **binary heap** instead of fully sorting the array.

## Approach: Min-Heap of Size k

We maintain a **min-heap** that always holds the `k` largest elements seen so far.

- For each element `num` in `arr`, push it onto the heap.
- If the heap grows larger than `k`, pop the **smallest** element (the root of a min-heap).
- After processing all elements, the heap contains exactly the `k` largest values. We sort them in descending order for the final output.

```python
import heapq

def KLargest(arr, k):
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)          # remove the current smallest
    return sorted(heap, reverse=True)    # k largest, largest first
```

### Why a Min-Heap?

The root of a min-heap is always the **smallest** among the stored elements. By keeping the heap size capped at `k`, the root continuously evicts smaller values, leaving only the `k` largest in the heap. A min-heap (not a max-heap) is the right choice here because we want to quickly discard the *smallest* of the kept elements.

## Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| Time | **O(n log k)** — each of the `n` insertions/deletions is O(log k) |
| Space | **O(k)** — the heap stores only `k` elements at any time |

> Compared to the sort-based approach (O(n log n) time, O(n) space), the heap method is faster when `k` is much smaller than `n`, and uses less memory.

## Examples

### Example 1
```
Input:  arr = [1, 23, 12, 9, 30, 2, 50], k = 3
Output: [50, 30, 23]
```

### Example 2
```
Input:  arr = [5, 1, 3], k = 3
Output: [5, 3, 1]
```

## Running the Tests

The `test.py` file uses Python's built-in `unittest` module and covers: basic case, `k = 1`, `k = n`, duplicates, single element, negative numbers, all-equal elements, and two elements.

```bash
python test.py
```

Expected output:
```
........
----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK
```

## Alternative Heap Approach: Max-Heap, Extract k Times

`heapq` only provides a min-heap, so a max-heap is simulated by negating values:

```python
import heapq

def KLargestMaxHeap(arr, k):
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)              # O(n)
    res = []
    for _ in range(k):
        res.append(-heapq.heappop(max_heap))   # extract max k times
    return res                          # already largest-first
```

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Min-heap of size k (this file) | O(n log k) | O(k) | Best when `k` is small |
| Max-heap, extract k times | O(n + k log n) | O(n) | Indexes whole array |
| Sort + slice (`Array/...`) | O(n log n) | O(n) | Simplest |

## Interview Questions

### Q1. Why not use a max-heap here?

**Answer**: A max-heap lets you extract the largest, but to get the `k` largest you would build a heap over all `n` elements (O(n) heapify) and pop `k` times (O(k log n)) — O(n + k log n) time and O(n) space. The min-heap-of-size-k trick is tighter: O(n log k) time and O(k) space, and particularly efficient for small `k`.

### Q2. Does this modify the input array?

**Answer**: No. Unlike the sort-based version, this approach pushes values into a separate heap and never mutates `arr`.

### Q3. What if `k > len(arr)`?

**Answer**: The code would return all elements sorted descending (the heap never exceeds `k`, but `k` is larger than the input). In practice you should guard with `k = min(k, len(arr))` or raise an error depending on problem constraints.

## File Structure

```
Heaps/
└── GFG_KLargest/
    ├── code.py    # KLargest using a min-heap of size k (heapq)
    ├── test.py    # Unit tests (unittest)
    └── README.md  # Documentation
```
