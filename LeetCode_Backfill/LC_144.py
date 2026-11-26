# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans = [] 
        right_ele = deque()
        curr = root 
        while right_ele or curr is not None:
            while curr is not None:
                ans.append(curr.val)
                if curr.right is not None:
                    right_ele.append(curr.right)
                curr = curr.left
            if right_ele :
                curr = right_ele.pop()
        return ans