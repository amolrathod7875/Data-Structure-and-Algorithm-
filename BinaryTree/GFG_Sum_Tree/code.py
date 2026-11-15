'''
# Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumTree(self, root):
        def check(root):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return root.data
            left_sum = check(root.left)
            if left_sum == -1:
                return -1
            right_sum = check(root.right)
            if right_sum == -1:
                return -1
            if root.data != left_sum + right_sum:
                return -1
            return root.data + left_sum + right_sum

        return check(root) != -1
