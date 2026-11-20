# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode | None:
        index_map = {val: i for i, val in enumerate(postorder)}
        pre_idx = 0

        def build(left, right):
            nonlocal pre_idx
            if left > right:
                return None
            root_val = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(root_val)

            if left == right:
                return root
            left_root = preorder[pre_idx]
            mid = index_map[left_root]

            root.left = build(left, mid)
            root.right = build(mid + 1, right - 1)

            return root

        return build(0, len(preorder) - 1)
