# Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, preorder):
        index_map = {val: i for i, val in enumerate(inorder)}
        pre_idx = [0]

        def build(left, right):
            if left > right:
                return None
            root_val = preorder[pre_idx[0]]
            pre_idx[0] += 1
            root = Node(root_val)
            mid = index_map[root_val]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)
