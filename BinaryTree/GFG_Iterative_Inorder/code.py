# Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def inOrder(self, root):
        ans = []
        stack = []
        curr = root
        while curr is not None or len(stack) > 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ans.append(curr.data)
            curr = curr.right
        return ans
