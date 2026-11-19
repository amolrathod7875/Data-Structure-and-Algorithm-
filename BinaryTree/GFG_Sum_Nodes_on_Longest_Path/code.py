# Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def sumOfLongRootToLeafPath(self, root: 'Node') -> int:
        def dfs(root):
            if not root:
                return (0, 0)

            left_len, left_sum = dfs(root.left)
            right_len, right_sum = dfs(root.right)

            if left_len > right_len:
                return (left_len + 1, left_sum + root.data)
            elif right_len > left_len:
                return (right_len + 1, right_sum + root.data)
            else:
                return (left_len + 1, max(left_sum, right_sum) + root.data)

        return dfs(root)[1]
