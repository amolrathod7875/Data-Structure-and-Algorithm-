# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        ans = [root.val]

        def helper(root, ans):
            if root is None:
                return 0
            l = max(0, helper(root.left, ans))
            r = max(0, helper(root.right, ans))

            ans[0] = max(ans[0], l + r + root.val)

            return root.val + max(l, r)

        helper(root, ans)

        return ans[0]
