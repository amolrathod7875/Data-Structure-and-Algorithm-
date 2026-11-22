class Solution:
    def mirror(self, root):
        """Mirror the tree in place; GFG supplies nodes with left/right fields."""
        if root is None:
            return

        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
