# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        level_max = {}
        ans = []
        def preorder(node, level):
            if node is None :
                return

            level_max[level] = max(level_max.get(level, node.val), node.val)

            preorder(node.left, level + 1)
            preorder(node.right, level + 1)

        preorder(root, 0)

        for level in level_max :
            ans.append(level_max[level])
        return ans
