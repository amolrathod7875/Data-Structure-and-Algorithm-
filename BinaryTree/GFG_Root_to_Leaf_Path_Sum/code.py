'''
# Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def hasPathSum(self, root, target):
        def traversal(root, path_sum):
            if root is None:
                return False
            path_sum += root.data
            if root.left is None and root.right is None:
                return path_sum == target
            return (
                traversal(root.left, path_sum) or
                traversal(root.right, path_sum)
            )

        return traversal(root, 0)
