# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def helper(root):
            if root is None:
                return 0

            left_node = helper(root.left)
            right_node = helper(root.right)

            if left_node == -1 or right_node == -1 or abs(left_node - right_node) > 1:
                return -1

            return max(left_node, right_node) + 1

        return helper(root) != -1
