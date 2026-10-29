# GFG Get Smaller in Array

## Problem

Given an array `arr` and a `target` value, return a **new** array containing only the elements of `arr` that are **strictly less than `target`**, preserving their original order.

```
result = [x for x in arr if x < target]
```

> Note: This is the same problem as **Elements Less Than K** (see `Array/GFG_Elements_Less_Than_K`), just with a different parameter name. The two solutions are identical.

---

## Examples

### Example 1

```
Input:  arr = [1, 2, 3, 4, 5], target = 4
Output: [1, 2, 3]
```

---

### Example 2

```
Input:  arr = [1, 2, 3, 4, 5], target = 1
Output: []
```

---

### Example 3

```
Input:  arr = [10, 20, 30], target = 25
Output: [10, 20]
```

---

## Approach: List Comprehension

### Key Insight

Filtering an array means keeping only the elements that satisfy a condition. In Python, a **list comprehension** is the idiomatic way to build a new list while filtering:

```python
[x for x in arr if x < target]
```

### Algorithm

1. Iterate over every element `x` in `arr`.
2. If `x < target`, include `x` in the result list.
3. Return the new list.

```python
class Solution:
    def getSmaller(self, arr, target):
        return [x for x in arr if x < target]
```

---

## Complexity Analysis

| | Time | Space |
|--|------|-------|
| **getSmaller** | **O(n)** — one pass over the `n` elements | **O(n)** — the result list holds up to `n` elements |

> Time is optimal: every element must be examined, so Ω(n) work is required.

---

## Flowchart

```mermaid
flowchart TD
    A["Input: arr array and target"] --> B["Create empty result list"]
    B --> C["For each x in arr"]
    C --> D{"x < target?"}
    D -->|Yes| E["Append x to result"]
    D -->|No| F["Skip x"]
    E --> G{"More elements?"}
    F --> G
    G -->|Yes| C
    G -->|No| H["Return result"]
```

---

## Example Test Case Trace

**Input:** `arr = [1, 2, 3, 4, 5]`, `target = 4`

| Step | x | x < 4? | result |
|------|---|--------|--------|
| 1 | 1 | Yes | `[1]` |
| 2 | 2 | Yes | `[1, 2]` |
| 3 | 3 | Yes | `[1, 2, 3]` |
| 4 | 4 | No | `[1, 2, 3]` |
| 5 | 5 | No | `[1, 2, 3]` |

**Final result:** `[1, 2, 3]`

---

## Run Tests

From the **repository root**:

```bash
python -m Array.GFG_Get_Smaller.test
```

Expected output:

```
=== GFG: Get Smaller in Array ===

PASS: getSmaller([1, 2, 3, 4, 5], 4)
  Expected: [1, 2, 3]
  Got:      [1, 2, 3]
...
```

The `test.py` covers: standard case, empty result, all elements kept, empty array, duplicates, negatives, single element, and boundary values.

---

## Alternative Approaches

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| List comprehension (this file) | O(n) | O(n) | Idiomatic; one line |
| `filter(lambda x: x < target, arr)` | O(n) | O(n) | Functional style; returns an iterator, needs `list()` |
| Manual `for` loop | O(n) | O(n) | Verbose; equivalent to the comprehension |

---

## Interview Questions

### Q1. Does this modify the input array?

**Answer**: No. The method builds and returns a **new** list; the original `arr` is untouched.

### Q2. What is the difference between `<` and `<=`?

**Answer**: `x < target` keeps elements **strictly** less than `target`. Use `x <= target` to also include elements equal to `target`.

### Q3. How is this related to `Array/GFG_Elements_Less_Than_K`?

**Answer**: They are the same problem with different parameter names. `getSmaller(arr, target)` and `elementsLessThanK(arr, k)` are functionally identical.

---

## File Structure

```
Array/
└── GFG_Get_Smaller/
    ├── code.py    # Solution.getSmaller using list comprehension
    ├── test.py    # Runnable tests (print-based assertions)
    └── README.md  # Documentation
```