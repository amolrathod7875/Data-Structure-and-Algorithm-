# GFG Height of Heap

## Problem Statement

Given a heap of size `N` (number of nodes), find its **height**.

A heap is a **complete binary tree**, so its height is determined entirely by the number of nodes `N` — the actual values stored don't matter.

## Approach

For a complete binary tree with `N` nodes, the height `h` (number of edges on the longest root-to-leaf path) is:

```
h = floor(log2(N))
```

An equivalent, GeeksforGeeks-friendly form that also handles `N = 0` cleanly is:

```
h = ceil(log2(N + 1) - 1)
```

Both expressions are mathematically identical for all `N >= 1`.

### Why this works

In a complete binary tree:
- Level `0` (root) holds `2^0 = 1` node
- Level `1` holds up to `2^1 = 2` nodes
- Level `i` holds up to `2^i` nodes

The tree reaches height `h` once it has at least `2^h` nodes and at most `2^(h+1) - 1` nodes. Solving `2^h <= N < 2^(h+1)` gives `h = floor(log2(N))`.

```python
import math

def height(N):
    return math.ceil(math.log2(N + 1) - 1)
```

### Note on `N = 0`

`height(0)` evaluates to `ceil(log2(1) - 1) = ceil(-1) = -1`, a common convention for an empty tree. Adjust to `0` if your problem defines empty-tree height as `0`.

## Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| Time | **O(1)** — a single `log2` computation |
| Space | **O(1)** — no extra data structures |

> This is optimal. A heap's height never needs to be built or traversed — it follows directly from the node count.

## Examples

| N | Height |
|---|--------|
| 1 | 0 |
| 2 | 1 |
| 3 | 1 |
| 4 | 2 |
| 6 | 2 |
| 7 | 2 |
| 8 | 3 |
| 15 | 3 |
| 16 | 4 |

```
Input:  N = 6
Output: 2

Tree (6 nodes):
         o
       /   \
      o     o
     / \
    o   o
Height (edges root -> deepest leaf) = 2
```

## Running the Tests

The `test.py` file uses Python's built-in `unittest` module and covers node counts from `0` to `16`, including the boundaries where height increments.

```bash
python test.py
```

Expected output:
```
..........
----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK
```

## Alternative Implementations

### Bit-length trick (no floating point)

```python
def height(N):
    return (N).bit_length() - 1 if N > 0 else -1
```

`N.bit_length()` returns `floor(log2(N)) + 1`, so subtracting `1` gives `floor(log2(N))`. This avoids any floating-point precision concerns for very large `N`.

### Brute-force (not recommended)

You could literally build a heap of `N` elements and then compute the height, but that is **O(N log N)** for an answer that is **O(1)**. The height depends only on the count `N`, never on the values, so building the heap is wasted work.

## Interview Questions

### Q1. Why is the height of a heap `floor(log2(N))` and not something else?

**Answer**: A heap is a complete binary tree, so each level `i` can hold at most `2^i` nodes. The smallest number of nodes that forces height `h` is `2^h` (fill level `h` minimally), and the largest that still fits in height `h` is `2^(h+1) - 1` (fill all levels up to `h`). Hence `2^h <= N < 2^(h+1)`, giving `h = floor(log2(N))`.

### Q2. Is heap height the same as the depth of the deepest node?

**Answer**: Yes, by the edge-count definition of height. The root is at depth `0`, and the height of the tree equals the maximum depth among its leaves.

### Q3. Does this change for a Min-Heap vs Max-Heap?

**Answer**: No. Height depends only on the tree's shape (it's complete), not on whether parents are smaller or larger than children.

## File Structure

```
Heaps/
└── GFG_Height_Of_Heap/
    ├── code.py    # height(N) using ceil(log2(N+1) - 1)
    ├── test.py    # Unit tests (unittest)
    └── README.md  # Documentation
```
