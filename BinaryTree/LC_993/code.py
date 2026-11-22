# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        info = {}

        def dfs(root, parent, depth):
            if root is None:
                return
            if root.val == x or root.val == y:
                info[root.val] = (parent, depth)
            dfs(root.left, root, depth + 1)
            dfs(root.right, root, depth + 1)

        dfs(root, None, 0)

        if x not in info or y not in info:
            return False

        px, dx = info[x]
        py, dy = info[y]

        return dx == dy and px != py
