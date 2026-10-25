# GFG Alternates in Array

## Problem

Given an array `arr`, return a new array containing the elements at even indices (0-based): indices 0, 2, 4, ...

## Examples

### Example 1

```
Input:  arr = [1, 2, 3, 4, 5]
Output: [1, 3, 5]
```

## Approach: Index Parity Filter

Iterate over the array; append element when its index is even.

```python
class Solution:
    def getAlternates(self, arr):
        result = []
        for i in range(len(arr)):
            if i % 2 == 0:
                result.append(arr[i])
        return result
```

## Complexity Analysis

| | Time | Space |
|--|------|-------|
| **getAlternates** | **O(n)** | **O(n/2)** |

## Run Tests

From the repository root:

```bash
python -m Array.Alternates_in_Array.test
```
