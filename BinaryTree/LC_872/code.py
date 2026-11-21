# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def getLeaves(root, result):
            if root is None:
                return
            if root.left is None and root.right is None:
                result.append(root.val)
            getLeaves(root.left, result)
            getLeaves(root.right, result)

        leaves1 = []
        leaves2 = []

        getLeaves(root1, leaves1)
        getLeaves(root2, leaves2)

        return leaves1 == leaves2
