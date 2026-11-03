# Sorting

Theory and implementations of common sorting algorithms.

## Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
| --- | --- | --- | --- | --- | --- |
| Bubble Sort | O(n) | O(n^2) | O(n^2) | O(1) | Yes |
| Selection Sort | O(n^2) | O(n^2) | O(n^2) | O(1) | No |
| Insertion Sort | O(n) | O(n^2) | O(n^2) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n^2) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting Sort | O(n + k) | O(n + k) | O(n + k) | O(k) | Yes |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n + k) | Yes |

## Key Concepts

- **Comparison-based sorts** (bubble, selection, insertion, merge, quick, heap) have a lower bound of Ω(n log n).
- **Non-comparison sorts** (counting, radix, bucket) can beat O(n log n) when key range is limited.
- **Stability**: equal elements retain original order (important for multi-key sorting).
- **In-place**: uses O(1) extra space (selection, insertion, heap, quick).
- **Divide and conquer**: merge sort and quick sort split then combine.

## When to Use

- Small / nearly sorted data: Insertion Sort.
- General purpose: Merge Sort (stable) or Quick Sort (fast average).
- Memory constrained: Heap Sort.
- Integer keys with small range: Counting / Radix Sort.

## Run

From repository root:

```bash
python -m Sorting.LC_910.test
```

## Working of Algorithms

### Bubble Sort
Repeatedly compare adjacent elements and swap if out of order. Largest element bubbles to the end each pass. Stop early if no swaps in a pass.

### Selection Sort
Find the minimum in the unsorted portion and swap it with the first unsorted position.

### Insertion Sort
Build a sorted prefix; take next element and insert it into correct position in prefix by shifting.

### Merge Sort
Divide array into halves, recursively sort, then merge two sorted halves by comparing front elements.

### Quick Sort
Pick a pivot, partition elements into <= pivot and > pivot, recursively sort both partitions.

### Heap Sort
Build a max-heap, repeatedly extract max to end, then heapify remaining.

### Counting Sort
Count occurrences of each key, compute prefix sums for positions, place elements into output in stable order.

### Radix Sort
Sort by least significant digit using a stable sort (e.g., counting sort), repeat for each digit.

## Step-by-Step Simulation

Example input: `[5, 3, 8, 4, 2]`

### Bubble Sort
- Pass 1: [3, 5, 4, 2, 8]
- Pass 2: [3, 4, 2, 5, 8]
- Pass 3: [3, 2, 4, 5, 8]
- Pass 4: [2, 3, 4, 5, 8]

### Selection Sort
- i=0: min 2 -> [2, 3, 8, 4, 5]
- i=1: min 3 -> [2, 3, 8, 4, 5]
- i=2: min 4 -> [2, 3, 4, 8, 5]
- i=3: min 5 -> [2, 3, 4, 5, 8]

### Insertion Sort
- Insert 3: [3, 5, 8, 4, 2]
- Insert 8: [3, 5, 8, 4, 2]
- Insert 4: [3, 4, 5, 8, 2]
- Insert 2: [2, 3, 4, 5, 8]

### Merge Sort
- Split: [5,3] [8,4,2]
- Sort halves: [3,5] [2,4,8]
- Merge: [2, 3, 4, 5, 8]

### Quick Sort (pivot = last)
- Partition around 2: [2 | 5,3,8,4] -> recurse left none, right [3,4,5,8]
- Result: [2, 3, 4, 5, 8]
