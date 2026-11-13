'
# Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'
class Solution:
    def maxWidth(self, root):
        level_count = {}
        
        def preorder(node, level):
            if node is None:
                return
            level_count[level] = level_count.get(level, 0) + 1
            preorder(node.left, level + 1)
            preorder(node.right, level + 1)
        
        preorder(root, 0)
        
        return max(level_count.values(), default=0)
