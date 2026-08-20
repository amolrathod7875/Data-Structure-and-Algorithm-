# K Largest Elements in an Array

## Problem Statement

Given an array `arr` and an integer `k`, return the **k largest elements** of the array.

This is a variation of the "Kth Largest Element" problem — instead of returning just the single k-th largest value, we return **all** `k` largest values.

## Approach: Sort and Slice

The simplest approach is to sort the array and then take a slice of the `k` largest elements.

- Python's built-in `list.sort()` uses **Timsort**, which sorts the array **in-place** in **ascending** order in **O(n log n)** time (guaranteed for all cases).
- After sorting ascending, the largest `k` elements are at the end of the array: `arr[-k:]`.
- We then reverse the slice with `[::-1]` so the result is returned in **descending** order (largest first).

```python
def KLargest(arr, k):
    arr.sort()            # Timsort, ascending, O(n log n) in-place
    return arr[-k:][::-1] # last k elements, reversed (largest first)
```

### Why `arr[-k:]`?

| k | Meaning | Slice |
|---|---------|-------|
| 1 | largest | `arr[-1:]` |
| 2 | two largest | `arr[-2:]` |
| k | k largest | `arr[-k:]` |

`[::-1]` reverses the selected slice so the output reads from biggest to smallest.

## Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| Time | **O(n log n)** — Timsort on `n` elements (worst/average/best) |
| Space | **O(n)** — Timsort needs temporary working space (sorts in-place w.r.t. the input array but uses extra memory internally) |

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

## Alternative Approaches (for comparison)

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sort + slice (this file) | O(n log n) | O(n) | Simplest; uses Timsort |
| Min-heap of size k | O(n log k) | O(k) | Best when `k` is small |
| Max-heap, extract k times | O(n + k log n) | O(1) | No full sort needed |
| **Quickselect + partial** | **O(n) avg** | O(1) | Fastest average; more code |

> For small `k` relative to `n`, the min-heap approach is more efficient since it avoids sorting the entire array.

## Interview Questions

### Q1. Does this modify the input array?

**Answer**: Yes. `arr.sort()` sorts the list **in-place**, so the original order of `arr` is lost after the call. To preserve it, operate on a copy: `sorted(arr)[-k:][::-1]`.

### Q2. What is the difference between this and "Kth Largest Element"?

**Answer**: "Kth Largest" returns a **single** value (the k-th largest). "K Largest Elements" returns **all** `k` largest values as a list.

### Q3. Why reverse the result with `[::-1]`?

**Answer**: Purely for output ordering — `arr[-k:]` is in ascending order (smallest of the chosen first). Reversing presents them from largest to smallest, which is the conventional, readable format.

## File Structure

```
Array/
└── k largest elements in an array/
    ├── code.py    # KLargest using list.sort()
    ├── test.py    # Unit tests (unittest)
    └── README.md  # Documentation
```
