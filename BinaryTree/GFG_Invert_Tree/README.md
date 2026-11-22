# GFG - Invert Tree (Convert to Mirror Tree)

[Practice problem](https://www.geeksforgeeks.org/problems/mirror-tree/1)

## Problem

Transform a binary tree into its mirror by exchanging the left and right child
of every node. Modify the existing nodes **in place**; return nothing.
GFG supplies the `Node` class with `data`, `left`, and `right` attributes.

| Level-order input (`N` means missing) | Mirrored level order |
| --- | --- |
| `[1, 2, 3, N, N, 4]` | `[1, 3, 2, N, 4]` |
| `[1, 2, 3, 4, 5]` | `[1, 3, 2, N, N, 5, 4]` |

Constraints: 1 to 10,000 nodes; node values are between 1 and 100,000.

## Approach: Iterative Depth-First Traversal

1. Put the root on a stack.
2. Remove a node and swap its child references.
3. Push its existing children to process their subtrees.
4. Continue until the stack is empty.

Each node is processed once, and every original edge is reversed to the opposite
child position. No nodes are copied or replaced. An explicit stack handles deep
trees without depending on Python's recursion limit.

Time: **O(n)**. Auxiliary space: **O(h)** for tree height `h`, **O(n)** worst case.

## Validation

Locally tested against both examples, an empty tree, a single node, duplicate
values, mirroring twice, and a 10,000-node chain. Tests check object identity and
child references as well as values. This solution has **not been submitted to
the GFG online judge** in this session.

Run from the repository root:

```bash
python -m BinaryTree.GFG_Invert_Tree.test
```
