# GFG Min Cost to Connect Ropes

## Problem Statement

Given an array `ropes[]` where `ropes[i]` is the length of the `i`-th rope, connect all ropes into a single rope. The cost to connect two ropes of lengths `a` and `b` is `a + b`. The cost of every connection is added to the total. Return the **minimum** total cost to connect all ropes into one.

This is equivalent to building a **Huffman tree** — the optimal strategy always combines the two **shortest** available ropes.

## Approach: Min-Heap (Huffman Coding)

Repeatedly pick the two smallest ropes, connect them, and put the resulting rope back into the pool. A **min-heap** makes it efficient to always fetch the two smallest lengths.

```python
import heapq

def minCost(ropes):
    if len(ropes) <= 1:
        return 0

    heap = ropes[:]          # copy so input is not mutated
    heapq.heapify(heap)      # O(n) build min-heap

    total = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)   # shortest
        b = heapq.heappop(heap)   # second shortest
        cost = a + b
        total += cost
        heapq.heappush(heap, cost)
    return total
```

### Worked Example — `ropes = [4, 3, 2, 6]`

| Step | Heap (min first) | Connect | Cost added | Running total |
|------|------------------|---------|------------|---------------|
| start | `[2, 3, 4, 6]` | — | — | 0 |
| 1 | pop 2, 3 → push 5 | 2 + 3 = 5 | 5 | 5 |
| 2 | `[4, 5, 6]` → pop 4, 5 → push 9 | 4 + 5 = 9 | 9 | 14 |
| 3 | `[6, 9]` → pop 6, 9 → push 15 | 6 + 9 = 15 | 15 | 29 |

Final total = **29** (matches GFG expected output).

### Why "shortest first"?

Connecting a short rope early means it gets re-added into future sums fewer times. By always combining the two smallest, we minimize how often longer ropes are counted — exactly the greedy optimality of Huffman coding.

## Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| Time | **O(n log n)** — each of the `n-1` connections does two pops and one push, each O(log n) |
| Space | **O(n)** — the heap stores up to `n` ropes |

## Examples

### Example 1
```
Input:  ropes = [4, 3, 2, 6]
Output: 29
```

### Example 2
```
Input:  ropes = [1, 2, 3, 4, 5]
Output: 33
```

## Running the Tests

The `test.py` file uses Python's built-in `unittest` module and covers: GFG example, five ropes, single/two ropes, all-equal, three ropes, sorted input, large values, and input-mutation safety.

```bash
python test.py
```

Expected output:
```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

## Alternative / Related

- **Priority Queue (max-heap)**: not suitable — we need the *smallest* two, so a min-heap is required.
- **Naive (no heap)**: repeatedly scanning for the two minimums gives O(n²), avoid for large inputs.
- This is the same greedy idea behind **Huffman Encoding** (data compression).

## Interview Questions

### Q1. Why is a min-heap needed instead of a max-heap?

**Answer**: We must always combine the two *shortest* ropes to keep repeated additions minimal. A min-heap gives O(log n) access to the smallest element; a max-heap would give the largest, which is the opposite of what the greedy optimum requires.

### Q2. What is the time complexity and why?

**Answer**: O(n log n). Building the heap is O(n). We perform `n - 1` merge steps; each step pops twice and pushes once — three O(log n) operations — so `(n-1) * O(log n) = O(n log n)`.

### Q3. Does this modify the input array?

**Answer**: No. The code copies the input with `ropes[:]` before heapifying, so the caller's list is unchanged. (A test in `test.py` verifies this.)

### Q4. What if there is only one rope?

**Answer**: No connections are needed, so the cost is `0`. The code guards this with `if len(ropes) <= 1: return 0`.

## File Structure

```
Heaps/
└── GFG_Min_Cost_to_Connect_Ropes/
    ├── code.py    # minCost using a min-heap (heapq)
    ├── test.py    # Unit tests (unittest)
    └── README.md  # Documentation
```
