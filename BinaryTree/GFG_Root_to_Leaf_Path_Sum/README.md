# GFG Root to Leaf Path Sum

Given a binary tree and a target sum, determine whether there exists a root-to-leaf path whose node values sum to the target.

## Problem Statement

You are given the root of a binary tree and an integer `target`. Write a function `hasPathSum(root, target)` that returns `True` if there is a path from root to a leaf where the sum of node values equals `target`, and `False` otherwise.

A **binary tree node** is defined as:

```python
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
```

## Theory

We can solve this with a recursive DFS. At each node, we add its value to the running sum. If we reach a leaf (both children `None`), we check if the running sum equals the target. Otherwise, we recurse on the left and right subtrees, returning `True` if either path succeeds.

## Algorithm

1. If `root` is `None`, return `False`.
2. Add `root.data` to `path_sum`.
3. If `root` is a leaf (both children `None`), return `path_sum == target`.
4. Otherwise, return `traversal(root.left, path_sum) OR traversal(root.right, path_sum)`.

## Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| Time   | **O(N)** – each node visited once |
| Space  | **O(H)** – recursion stack depth |

## Implementation

```python
'''
# Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def hasPathSum(self, root, target):
        def traversal(root, path_sum):
            if root is None:
                return False
            path_sum += root.data
            if root.left is None and root.right is None:
                return path_sum == target
            return (
                traversal(root.left, path_sum) or
                traversal(root.right, path_sum)
            )

        return traversal(root, 0)
```

## Examples

### Example 1
```
Input:
     5
   /   \
  4     8
 /     / \
11    13  4
/ \       \
7   2       1

target = 22
Path: 5 -> 4 -> 11 -> 2 = 22
Output: True
```

### Example 2
```
Input:
     1
   /   \
  2     3

target = 5
No root-to-leaf path sums to 5.
Output: False
```

## Running the Tests

Run tests from the repository root:

```bash
PYTHONPATH=. python BinaryTree/GFG_Root_to_Leaf_Path_Sum/test.py
```

Expected output:

```
=== GFG: Root to Leaf Path Sum ===

PASS: hasPathSum([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22)
  Expected: True
  Got:      True

PASS: hasPathSum([1, 2, 3], 5)
  Expected: False
  Got:      False

PASS: hasPathSum([1, 2], 3)
  Expected: True
  Got:      True

PASS: hasPathSum([1], 1)
  Expected: True
  Got:      True

PASS: hasPathSum([], 0)
  Expected: False
  Got:      False

All GFG_Root_to_Leaf_Path_Sum tests passed.
```

## File Structure

```
BinaryTree/
└── GFG_Root_to_Leaf_Path_Sum/
    ├── code.py    # Node and Solution implementation
    ├── test.py    # Unit tests
    └── README.md  # Documentation
```

```mermaid
flowchart TD
    A["Start"] --> B{"Is root None?"}
    B -->|Yes| C["Return False"]
    B -->|No| D["path_sum += root.data"]
    D --> E{"Is leaf?"}
    E -->|Yes| F{"path_sum == target?"}
    F -->|Yes| G["Return True"]
    F -->|No| H["Return False"]
    E -->|No| I["Recurse left"]
    I --> J["Recurse right"]
    J --> K["Return left OR right"]
    C --> K
```
