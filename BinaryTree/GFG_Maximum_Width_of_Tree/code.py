"""
# Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def maxWidth(self, root):
        if not root:
            return 0
        
        queue = [(root, 0)]
        level_count = {}
        
        while queue:
            node, level = queue.pop(0)
            level_count[level] = level_count.get(level, 0) + 1
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return max(level_count.values())
