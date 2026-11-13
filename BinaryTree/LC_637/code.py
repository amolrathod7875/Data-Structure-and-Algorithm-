# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        level_sum = {}
        level_count = {}
        ans = []

        def preorder(node, level):
            if node is None :
                return
            
            level_sum[level] = level_sum.get(level, 0) + node.val
            level_count[level] = level_count.get(level, 0) + 1 

            preorder(node.left, level + 1 )
            preorder(node.right, level + 1 )
        
        preorder(root, 0)

        for level in level_sum :
            avg = level_sum[level] / level_count[level]
            ans.append(avg)
        return ans
