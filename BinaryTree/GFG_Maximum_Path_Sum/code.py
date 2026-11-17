'''
# Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxSum(self, root):
        if root is None:
            return 0

        ans = [root.data]

        def helper(root, ans):
            if root is None:
                return 0
            l = max(0, helper(root.left, ans))
            r = max(0, helper(root.right, ans))
            ans[0] = max(ans[0], l + r + root.data)
            return root.data + max(l, r)

        helper(root, ans)

        return ans[0]
