# Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def noSibling(self, root):
        result = []

        def helper(root, result):
            if root is None:
                return
            if root.left and root.right:
                helper(root.left, result)
                helper(root.right, result)
            elif root.left:
                result.append(root.left.data)
                helper(root.left, result)
            elif root.right:
                result.append(root.right.data)
                helper(root.right, result)

        helper(root, result)

        if not result:
            result.append(-1)
        else:
            result.sort()

        return result
