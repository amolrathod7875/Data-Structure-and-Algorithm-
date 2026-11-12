# Definition for a binary tree node.
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def height(self, root):
        if root is None:
            return -1
        left = self.height(root.left)
        right = self.height(root.right)
        return 1 + max(left, right)