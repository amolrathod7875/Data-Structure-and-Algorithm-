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
