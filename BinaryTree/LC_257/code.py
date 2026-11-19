# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        result = []

        def dfs(root, path):
            if not root:
                return
            path += str(root.val)
            if root.left is None and root.right is None:
                result.append(path)
                return
            dfs(root.left, path + "->")
            dfs(root.right, path + "->")

        dfs(root, "")
        return result
