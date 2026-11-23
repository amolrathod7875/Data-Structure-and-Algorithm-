# LC 226 - Invert Binary Tree

[LeetCode problem](https://leetcode.com/problems/invert-binary-tree/)

Python 3: **Accepted, 77/77 tests**, 23 November 2026.
[Accepted submission](https://leetcode.com/problems/invert-binary-tree/submissions/2201982885/)

## Problem

Exchange the left and right child of every node in a binary tree, then return
the original root. An empty tree returns `None`. The tree has 0 to 100 nodes,
with values from -100 to 100.

| Level-order input | Output |
| --- | --- |
| `[4, 2, 7, 1, 3, 6, 9]` | `[4, 7, 2, 9, 6, 3, 1]` |
| `[2, 1, 3]` | `[2, 3, 1]` |
| `[]` | `[]` |

## Approach: Iterative DFS

Process nodes with a stack. Swap each node's children and push its existing
children. Each original node is processed exactly once, so every pair of child
references is exchanged. The root and all node identities are preserved.

Time: **O(n)**. Auxiliary space: **O(h)**, at most **O(n)**.

## GFG Connection

[GFG Convert to Mirror Tree](https://www.geeksforgeeks.org/problems/mirror-tree/1)
uses the same traversal and swaps. GFG's `mirror(root)` modifies the tree and
returns nothing; LeetCode's `invertTree(root)` returns the root. The related
implementation is in `BinaryTree/GFG_Invert_Tree`.

The local module postpones type annotation evaluation so the judge-provided
`TreeNode` type does not need to be defined when importing it for tests.

## Run Tests

```bash
python -m unittest BinaryTree.LC_226.test -v
```

Tests cover all examples, one-sided trees, duplicate and negative values,
identity preservation, and restoring the exact structure by inverting twice.
