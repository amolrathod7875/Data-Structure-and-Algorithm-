# GFG Kth Largest Element

## Problem Statement

Given an array `nums` and an integer `k`, return the **k-th largest** element in the array.

> Note: This is the same problem as **LeetCode 215 (Kth Largest Element in an Array)**. The GFG version is typically phrased identically.

## Approach: Sort and Index

The simplest approach is to sort the array and then directly pick the k-th largest element.

- Python's built-in `list.sort()` uses **Timsort** (a hybrid of Merge Sort and Insertion Sort), which sorts the array **in-place** in **ascending** order in **O(n log n)** time (guaranteed, all cases).
- In a sorted (ascending) array, the **largest** element is at the last index `n - 1`, the 2nd largest at `n - 2`, and so on. Therefore, the k-th largest element is at index `-(k)` from the end, i.e. `nums[-k]`.

```python
def findkthlargest(nums, k):
    nums.sort()      # Timsort, ascending, O(n log n) in-place
    return nums[-k]  # k-th largest = k-th from the end
```

### Why `nums[-k]`?

| k | Meaning | Index |
|---|---------|-------|
| 1 | largest | `nums[-1]` |
| 2 | 2nd largest | `nums[-2]` |
| k | k-th largest | `nums[-k]` |

## Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| Time | **O(n log n)** — Timsort on `n` elements (worst, average, and best) |
| Space | **O(n)** — Timsort requires temporary working space; sorts in-place w.r.t. the input array but uses extra memory internally |

> While this is clean and easy to write, it does more work than necessary: we only need one element, not a fully sorted array. A **Quickselect**-based solution achieves **average O(n)** time, and a **min-heap of size k** achieves **O(n log k)**. Sorting is O(n log n) but is often fast enough in practice thanks to Timsort's optimizations.

## Examples

### Example 1
```
Input:  nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
```

### Example 2
```
Input:  nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4
```

## Running the Tests

The `test.py` file uses Python's built-in `unittest` module and covers: basic case, `k = 1`, `k = n`, duplicates, single element, negative numbers, two elements, and all-equal elements.

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

## Alternative Approaches (for comparison)

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sort + index (this file) | O(n log n) | O(n) | Simplest; uses Timsort |
| Min-heap of size k | O(n log k) | O(k) | Good when k is small |
| Max-heap, extract k-1 | O(n + k log n) | O(1) | See `Heaps/LC_215` |
| **Quickselect** | **O(n) avg** (O(n²) worst) | O(1) | Fastest average; no full sort |

## Interview Questions

### Q1. Does this approach modify the input array?

**Answer**: Yes. `nums.sort()` sorts the list **in-place**, so the original order of `nums` is lost after the call. If you need to preserve it, pass a copy: `sorted(nums)[-k]`.

### Q2. What is `list.sort()` vs `sorted()`?

**Answer**: `list.sort()` sorts in-place and returns `None`. `sorted(iterable)` returns a new sorted list without modifying the original. Both use Timsort (O(n log n)).

### Q3. Why not use Quickselect here?

**Answer**: You can, and it's faster on average (O(n)). But the sort-based method is shorter, less error-prone, and Timsort is highly optimized in C, so for moderate inputs it's often just as fast in practice while being far simpler to write and verify.

## File Structure

```
Array/
└── GFG_Kth_Largest_element/
    ├── code.py    # findkthlargest using list.sort()
    ├── test.py    # Unit tests (unittest)
    └── README.md  # Documentation
```
