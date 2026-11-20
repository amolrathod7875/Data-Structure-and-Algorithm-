# Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def boundaryTraversal(self, root):
        if not root:
            return []

        result = []

        def isLeaf(node):
            return not node.left and not node.right

        # Step 1: Add root
        result.append(root.data)

        if isLeaf(root):
            return result

        # Step 2: Add left boundary
        curr = root.left

        while curr:
            if not isLeaf(curr):
                result.append(curr.data)

            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

        # Step 3: Add all leaf nodes
        def addLeaves(node):
            if not node:
                return

            if isLeaf(node):
                result.append(node.data)
                return

            addLeaves(node.left)
            addLeaves(node.right)

        addLeaves(root)

        # Step 4: Add right boundary in reverse
        curr = root.right
        right_boundary = []

        while curr:
            if not isLeaf(curr):
                right_boundary.append(curr.data)

            if curr.right:
                curr = curr.right
            else:
                curr = curr.left

        result.extend(reversed(right_boundary))

        return result
