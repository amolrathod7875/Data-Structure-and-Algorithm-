'''
# Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def rightView(self, root):
        level_right = {}
        ans = []

        def right_order(root, level):
            if root is None:
                return
            if level not in level_right:
                level_right[level] = root.data

            right_order(root.right, level + 1)
            right_order(root.left, level + 1)

        right_order(root, 0)

        for level in level_right:
            ans.append(level_right[level])

        return ans
