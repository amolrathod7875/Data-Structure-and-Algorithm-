# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: TreeNode | None) -> list[int]:
        ans = []
        freq = {}

        def dfs(root):
            if root is None:
                return 0
            left_sum = dfs(root.left)
            right_sum = dfs(root.right)
            total_sum = left_sum + right_sum + root.val

            freq[total_sum] = freq.get(total_sum, 0) + 1

            return total_sum

        dfs(root)

        if not freq:
            return []

        max_freq = max(freq.values())
        for subtree_sum, count in freq.items():
            if count == max_freq:
                ans.append(subtree_sum)

        return ans
