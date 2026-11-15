'''
# Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def leftView(self, root):
        level_left = {}
        ans = []

        def left_order(root, level):
            if root is None:
                return
            if level not in level_left:
                level_left[level] = root.data
            left_order(root.left, level + 1)
            left_order(root.right, level + 1)

        left_order(root, 0)

        for level in level_left:
            ans.append(level_left[level])
        return ans
