# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def traversal(root, path_sum):
            if root is None:
                return False
            path_sum += root.val
            if root.left is None and root.right is None:
                return path_sum == targetSum
            return (
                traversal(root.left, path_sum) or
                traversal(root.right, path_sum)
            )

        return traversal(root, 0)
