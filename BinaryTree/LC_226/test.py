from collections import deque
import unittest

from BinaryTree.LC_226.code import Solution


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    values = iter(values[1:])
    while queue:
        node = queue.popleft()
        for side in ('left', 'right'):
            value = next(values, None)
            if value is not None:
                child = TreeNode(value)
                setattr(node, side, child)
                queue.append(child)
    return root


def level_order(root):
    result = []
    queue = deque([root]) if root else deque()
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.extend([node.left, node.right])
    while result and result[-1] is None:
        result.pop()
    return result


class InvertTests(unittest.TestCase):
    def test_examples(self):
        for values, expected in [
            ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
            ([2, 1, 3], [2, 3, 1]),
            ([], []),
        ]:
            root = build(values)
            self.assertIs(Solution().invertTree(root), root)
            self.assertEqual(level_order(root), expected)

    def test_single_node(self):
        root = TreeNode(-100)
        self.assertIs(Solution().invertTree(root), root)
        self.assertEqual(level_order(root), [-100])

    def test_one_sided_tree(self):
        root = build([1, 2, None, 3])
        self.assertEqual(level_order(Solution().invertTree(root)), [1, None, 2, None, 3])

    def test_node_identity_and_double_inversion(self):
        root = build([0, -1, -1, 2, None, 2, 3])
        before = {}
        stack = [root]
        while stack:
            node = stack.pop()
            before[node] = (node.val, node.left, node.right)
            stack.extend(x for x in (node.left, node.right) if x is not None)
        Solution().invertTree(root)
        for node, (value, left, right) in before.items():
            self.assertEqual(node.val, value)
            self.assertIs(node.left, right)
            self.assertIs(node.right, left)
        Solution().invertTree(root)
        for node, (value, left, right) in before.items():
            self.assertEqual(node.val, value)
            self.assertIs(node.left, left)
            self.assertIs(node.right, right)


if __name__ == '__main__':
    unittest.main(verbosity=2)
