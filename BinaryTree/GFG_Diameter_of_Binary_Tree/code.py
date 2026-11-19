# Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def diameter(self, root):
        if root is None:
            return 0
        max_height = 0

        def dfs(root):
            nonlocal max_height
            if root is None:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)

            max_height = max(max_height, left_height + right_height)

            return 1 + max(left_height, right_height)

        dfs(root)
        return max_height
