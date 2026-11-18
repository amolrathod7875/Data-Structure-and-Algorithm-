# Binary Tree Node Structure
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def preOrder(self, root):
        from collections import deque
        ans = []
        right_ele = deque()
        curr = root
        while right_ele or curr is not None:
            while curr is not None:
                ans.append(curr.data)
                if curr.right is not None:
                    right_ele.append(curr.right)
                curr = curr.left

            if right_ele:
                curr = right_ele.pop()
        return ans
