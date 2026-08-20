# Check if an Array is Max Heap

## Problem Statement

Given an array `arr` of size `N`, check if it represents a **Max Heap**.

A **Max Heap** is a complete binary tree where the value of each parent node is **greater than or equal to** the values of its children.

For a node at index `i` in the array representation:
- Left child index = `2 * i + 1`
- Right child index = `2 * i + 2`

## Theory

A binary heap stored in an array is a **complete binary tree**, meaning all levels are fully filled except possibly the last, which is filled from left to right. Because of this property, heaps can be efficiently stored in arrays without pointers.

### Max Heap Property

For every node `i`:
```
arr[i] >= arr[2*i + 1]   (left child)
arr[i] >= arr[2*i + 2]   (right child)
```

### Key Insight

Only **internal nodes** (non-leaf nodes) need to be checked. In a 0-indexed array, internal nodes are located at indices `0` to `(n // 2) - 1`. Nodes from `n // 2` onwards are leaf nodes and have no children.

## Algorithm

1. Calculate the number of internal nodes: `n // 2`
2. Iterate through each internal node `i` from `0` to `n // 2 - 1`
3. Compute left child index `l = 2 * i + 1` and right child index `r = 2 * i + 2`
4. Check bounds to avoid `IndexError` for leaf nodes with missing children
5. If `arr[i] < arr[l]` or `arr[i] < arr[r]`, return `False`
6. If all internal nodes satisfy the heap property, return `True`

## Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| Time   | O(n) — we visit each internal node once |
| Space  | O(1) — no extra data structures used |

## Implementation

```python
def isMaxHeap(arr):
    n = len(arr)
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            return False
        if right < n and arr[i] < arr[right]:
            return False
    return True
```

## Examples

### Example 1: Valid Max Heap

```
Input:  arr = [90, 15, 10, 7, 12, 2]
Output: True

Tree representation:
        90
      /    \
    15      10
   /  \    /
  7    12  2
```

### Example 2: Invalid Max Heap

```
Input:  arr = [9, 15, 10, 7, 12, 11]
Output: False

Tree representation:
        9
      /    \
    15      10
   /  \    /
  7    12  11

Root (9) is smaller than its left child (15), violating the max heap property.
```

## Common Use Cases

1. **Heap Validation** — verify that a given array maintains heap properties after heapify operations
2. **Priority Queue Verification** — ensure underlying heap implementation is correct
3. **Competitive Programming** — common problem on platforms like GeeksforGeeks, LeetCode

## Interview Questions

### Q1. Why do we only check up to `n // 2`?

**Answer**: Nodes from index `n // 2` onwards are leaf nodes in a complete binary tree. Leaf nodes have no children, so the heap property trivially holds for them. We only need to verify internal nodes.

### Q2. What happens if we don't check array bounds for children?

**Answer**: For nodes near the end of the array, one or both children may not exist. Accessing `arr[right]` without bounds checking will raise an `IndexError`.

### Q3. Is this approach valid for MinHeap as well?

**Answer**: Yes, the same structure applies. For a MinHeap, the condition changes to `arr[i] > arr[left]` or `arr[i] > arr[right]`.

## File Structure

```
Heaps/
└── GFG_Check if an Array is Max Heap/
    ├── code.py    # isMaxHeap implementation
    ├── test.py    # Unit tests
    └── README.md  # Documentation
```
