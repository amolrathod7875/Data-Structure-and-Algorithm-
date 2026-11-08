# LC 189 - Rotate Array

## Problem

Given an integer array `nums` and an integer `k`, **rotate the array to the right by `k` steps**.

A right rotation by `k` moves the last `k` elements to the front, keeping their relative order, and shifts the remaining elements to the right:

```
nums = [a1, a2, ..., an]  ->  [a(n-k+1), ..., an, a1, a2, ..., a(n-k)]
```

The rotation is performed **in place**, so `rotate` mutates `nums` and returns `None`.

**Constraints:**

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

---

## Subfolders

This problem has **two implementations** using different approaches:

| Subfolder | Approach | Time | Space | Description |
|-----------|----------|------|-------|-------------|
| [`Three_Reversals/`](Three_Reversals/) | Three reversals | O(n) | O(1) | Optimal in place; reverses whole array, then first k, then rest |
| [`Slicing/`](Slicing/) | List slicing | O(n) | O(n) | Simplest; `nums[:] = nums[-k:] + nums[:-k]` |

Both produce identical results. Choose based on your constraints:
- **Memory-constrained** → `Three_Reversals/` (O(1) extra space)
- **Readability-first** → `Slicing/` (one line of logic)

---

## Examples

### Example 1

```
Input:  nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Output: [5, 6, 7, 1, 2, 3, 4]
```

---

### Example 2

```
Input:  nums = [-1, -100, 3, 99], k = 2
Output: [3, 99, -1, -100]
```

---

### Example 3

```
Input:  nums = [1, 2, 3], k = 3
Output: [1, 2, 3]
```

---

## Run Tests

From the **repository root**:

```bash
# Three reversals approach
python -m Array.LC_189.Three_Reversals.test

# Slicing approach
python -m Array.LC_189.Slicing.test
```

---

## File Structure

```
Array/
└── LC_189/
    ├── README.md              # This file (problem overview)
    ├── Three_Reversals/
    │   ├── code.py            # Solution.rotate using three reversals
    │   ├── test.py            # Runnable tests (print-based assertions)
    │   └── README.md          # Detailed docs for reversal approach
    └── Slicing/
        ├── code.py            # Solution.rotate using list slicing
        ├── test.py            # Runnable tests (print-based assertions)
        └── README.md          # Detailed docs for slicing approach
```