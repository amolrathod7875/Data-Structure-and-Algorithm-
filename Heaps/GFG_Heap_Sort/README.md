# GFG Heap Sort

Heap Sort is a comparison-based sorting algorithm that uses a **Binary Heap** data structure. It divides the input into a sorted and an unsorted region, and iteratively shrinks the unsorted region by extracting the largest element (in a Max Heap) and placing it at the end.

## Problem Statement

Given an array `arr` of size `n`, sort it in **ascending** order using Heap Sort.

A **Max Heap** is a complete binary tree where the value of each parent node is **greater than or equal to** the values of its children. In array representation (0-indexed):

- Left child of node `i`  → `2 * i + 1`
- Right child of node `i` → `2 * i + 2`
- Parent of node `i`      → `(i - 1) // 2`

## Theory

Heap Sort works in two main phases:

1. **Build Max Heap** — rearrange the array so that it satisfies the max-heap property. Because a complete binary tree's last internal node sits at index `(n // 2) - 1`, we call `heapify` in reverse order over all internal nodes.
2. **Extract Elements** — repeatedly swap the root (largest element) with the last element of the heap, reduce the heap size, and `heapify` the new root. This places the next-largest element at its final sorted position, working from the end of the array toward the front.

### Heapify

`heapify(arr, n, i)` ensures the subtree rooted at index `i` is a max heap. It compares the root with its children; if a child is larger, it swaps and recursively heapifies the affected subtree.

## Algorithm

```
heapify(arr, n, i):
    largest = i
    left  = 2*i + 1
    right = 2*i + 2

    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        swap arr[i] and arr[largest]
        heapify(arr, n, largest)

heapSort(arr):
    n = len(arr)
    for i = n//2 - 1 down to 0:
        heapify(arr, n, i)
    for i = n - 1 down to 1:
        swap arr[0] and arr[i]
        heapify(arr, i, 0)
```

## Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| Time (build heap) | O(n) |
| Time (extract phase) | O(n log n) |
| Time (overall) | **O(n log n)** in all cases (best, average, worst) |
| Space | **O(1)** — in-place, no extra data structures |

> Unlike Quick Sort, Heap Sort's running time is guaranteed O(n log n); unlike Merge Sort, it needs only O(1) auxiliary space.

## Implementation

```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
```

## Examples

### Example 1
```
Input:  arr = [12, 11, 13, 5, 6, 7]
Output: [5, 6, 7, 11, 12, 13]
```

### Example 2
```
Input:  arr = [4, 2, 4, 3, 2, 1]
Output: [1, 2, 2, 3, 4, 4]
```

### Example 3
```
Input:  arr = [-3, -1, -2, -5, 0]
Output: [-5, -3, -2, -1, 0]
```

## Running the Tests

The `test.py` file uses Python's built-in `unittest` module and covers: basic case, already sorted, reverse sorted, duplicates, single element, empty array, negative numbers, and a larger mixed array.

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

## Common Use Cases

1. **In-place sorting** — when memory is constrained and a guaranteed O(n log n) bound is required.
2. **Priority Queue internals** — the same heapify logic underpins `heapq` and priority queues.
3. **Systems programming** — predictable worst-case performance (unlike Quick Sort).

## Interview Questions

### Q1. Why is the time complexity of Heap Sort always O(n log n)?

**Answer**: Building the heap takes O(n). Each of the `n` extract-max steps calls `heapify`, which takes O(log n). So the total is O(n + n log n) = O(n log n) in the best, average, and worst cases.

### Q2. Is Heap Sort stable?

**Answer**: No. Swapping the root with the last element can change the relative order of equal keys, so Heap Sort is not a stable sort.

### Q3. Why do we start the build-heap loop at `n // 2 - 1`?

**Answer**: Nodes from index `n // 2` onward are leaf nodes (they have no children), so heapifying them is a no-op. The last internal node is at index `(n // 2) - 1`.

### Q4. What is the space complexity of Heap Sort?

**Answer**: O(1) auxiliary space because the sorting is done in-place within the input array. (Note: the recursive `heapify` uses O(log n) call-stack space; an iterative heapify keeps it strictly O(1).)

## File Structure

```
Heaps/
└── GFG_Heap_Sort/
    ├── code.py    # heapSort and heapify implementation
    ├── test.py    # Unit tests (unittest)
    └── README.md  # Documentation
```
