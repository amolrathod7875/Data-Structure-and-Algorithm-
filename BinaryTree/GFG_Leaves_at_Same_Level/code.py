# Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def check(self, root):
        def minDist(curr):
            if curr is None:
                return 0

            if curr.left is None:
                return 1 + minDist(curr.right)

            if curr.right is None:
                return 1 + minDist(curr.left)

            return 1 + min(
                minDist(curr.left),
                minDist(curr.right)
            )

        def maxDist(curr):
            if curr is None:
                return 0

            return 1 + max(
                maxDist(curr.left),
                maxDist(curr.right)
            )

        max_dist = maxDist(root)
        min_dist = minDist(root)

        return max_dist == min_dist
