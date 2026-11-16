# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result = []

        def traversal(root, path_sum, path):
            if root is None:
                return

            path_sum += root.val
            path.append(root.val)

            if root.left is None and root.right is None:
                if path_sum == targetSum:
                    result.append(path.copy())

            traversal(root.left, path_sum, path)
            traversal(root.right, path_sum, path)

            path.pop()

        traversal(root, 0, [])
        return result
