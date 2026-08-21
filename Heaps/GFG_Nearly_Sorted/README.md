# GFG Nearly Sorted (K-Sorted) Array

## Problem Statement

Given an array `arr` that is **nearly sorted** (also called **k-sorted**), sort it completely. An array is k-sorted when **every element is at most `k` positions away from its correct position** in the fully sorted array.

> Example: with `k = 2`, the value that belongs at index `0` can only be found in indices `0, 1, or 2`.

## Approach: Min-Heap of Size k+1

Because the smallest overall element must lie within the first `k + 1` positions, we maintain a **min-heap** holding a sliding window of at most `k + 1` elements. Repeatedly popping the heap's minimum yields the next sorted value, and we push the next unseen array element to keep the window full.

```python
import heapq

def sortNearlySorted(arr, k):
    n = len(arr)
    heap = arr[:k + 1]
    heapq.heapify(heap)          # O(k)

    result = []
    idx = k + 1
    for i in range(n):
        result.append(heapq.heappop(heap))   # smallest in current window
        if idx < n:
            heapq.heappush(heap, arr[idx])   # slide window right
            idx += 1
    return result
```

### Why `k + 1`?

The element that belongs at the front of the sorted array is at most `k` positions away, so it must be among `arr[0..k]` — exactly `k + 1` candidates. Keeping the window that wide guarantees the true next-minimum is always inside the heap.

### Worked Example — `arr = [2, 1, 4, 3, 6, 5]`, `k = 1`

| Step | Heap (min first) | Pop | Push | Result |
|------|------------------|-----|------|--------|
| init | `[1, 2, 4]` | — | — | `[]` |
| 1 | pop 1 | — | push 3 → `[2,3,4]` | `[1]` |
| 2 | pop 2 | — | push 6 → `[3,4,6]` | `[1,2]` |
| 3 | pop 3 | — | push 5 → `[4,5,6]` | `[1,2,3]` |
| 4 | pop 4 | — | (none) → `[5,6]` | `[1,2,3,4]` |
| 5 | pop 5 | — | (none) → `[6]` | `[1,2,3,4,5]` |
| 6 | pop 6 | — | — | `[1,2,3,4,5,6]` |

Final: **`[1, 2, 3, 4, 5, 6]`** ✓

## Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| Time | **O(n log k)** — `n` heap operations, each O(log k) |
| Space | **O(k)** — the heap holds at most `k + 1` elements |

> Compare to a full `arr.sort()` which is **O(n log n)**. When `k` is small relative to `n` (the whole point of "nearly sorted"), the heap method is much faster and uses far less memory.

## Examples

### Example 1
```
Input:  arr = [2, 1, 4, 3, 6, 5], k = 1
Output: [1, 2, 3, 4, 5, 6]
```

### Example 2
```
Input:  arr = [6, 5, 3, 2, 8, 10, 9], k = 3
Output: [2, 3, 5, 6, 8, 9, 10]
```

## Running the Tests

The `test.py` file uses Python's built-in `unittest` module and covers: `k = 0` (already sorted), `k = 1`, `k = 2`, a GFG-style example, single element, duplicates, negative numbers, and input-mutation safety.

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

## Alternative Approaches

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Min-heap window (this file) | O(n log k) | O(k) | Optimal for k-sorted input |
| `arr.sort()` (Timsort) | O(n log n) | O(n) | Simplest, ignores the k-sorted property |
| Insertion Sort | O(nk) | O(1) | Works but slower than the heap when k is moderate |

## Interview Questions

### Q1. Why is the window size `k + 1` and not `k`?

**Answer**: An element can be up to `k` positions to the *right* of its sorted spot. The element that belongs at index `0` could be at index `k`, so we must look at indices `0..k` inclusive — that's `k + 1` elements — to be certain the true minimum is in the heap.

### Q2. What is the time complexity and why?

**Answer**: O(n log k). We run `n` iterations; each does one `heappop` and at most one `heappush`, both O(log k). Heapify of the initial `k+1` elements is O(k), dominated by the loop.

### Q3. Does this modify the input array?

**Answer**: No. The code copies the initial window with `arr[:k+1]` and builds a separate `result` list, leaving `arr` unchanged. (A test in `test.py` verifies this.)

### Q4. Is this a LeetCode problem?

**Answer**: This exact "nearly sorted" formulation is a classic **GeeksforGeeks** problem. The same min-heap sliding-window technique is also the core idea behind **LeetCode 23 (Merge k Sorted Lists)** and **LC 1439**, and it directly applies to **LC 1167 (Min Cost to Connect Sticks)**'s heap usage patterns.

## File Structure

```
Heaps/
└── GFG_Nearly_Sorted/
    ├── code.py    # sortNearlySorted using a min-heap of size k+1
    ├── test.py    # Unit tests (unittest)
    └── README.md  # Documentation
```
