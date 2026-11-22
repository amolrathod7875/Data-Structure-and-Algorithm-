from collections import deque
import unittest

from BinaryTree.GFG_Invert_Tree.code import Solution


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(values):
    if not values:
        return None
    root = Node(values[0])
    nodes = deque([root])
    values = iter(values[1:])
    while nodes:
        node = nodes.popleft()
        for side in ("left", "right"):
            value = next(values, None)
            if value is not None:
                child = Node(value)
                setattr(node, side, child)
                nodes.append(child)
    return root


def level_order(root):
    if root is None:
        return []
    result = []
    nodes = deque([root])
    while nodes:
        node = nodes.popleft()
        if node is None:
            result.append(None)
        else:
            result.append(node.data)
            nodes.extend([node.left, node.right])
    while result and result[-1] is None:
        result.pop()
    return result


def snapshot(root):
    result = {}
    nodes = [root] if root is not None else []
    while nodes:
        node = nodes.pop()
        result[node] = (node.data, node.left, node.right)
        nodes.extend(child for child in (node.left, node.right) if child is not None)
    return result


class MirrorTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        examples = [
            ([1, 2, 3, None, None, 4], [1, 3, 2, None, 4]),
            ([1, 2, 3, 4, 5], [1, 3, 2, None, None, 5, 4]),
        ]
        for values, expected in examples:
            with self.subTest(values=values):
                root = build_tree(values)
                self.assertIsNone(self.solution.mirror(root))
                self.assertEqual(level_order(root), expected)

    def test_empty_tree(self):
        self.assertIsNone(self.solution.mirror(None))

    def test_single_node(self):
        root = Node(7)
        before = snapshot(root)
        self.solution.mirror(root)
        self.assertEqual(snapshot(root), before)

    def test_reuses_nodes_and_swaps_every_edge(self):
        root = build_tree([1, 2, 2, None, 3, 3, 4])
        before = snapshot(root)
        self.solution.mirror(root)
        self.assertEqual(set(snapshot(root)), set(before))
        for node, (value, left, right) in before.items():
            self.assertEqual(node.data, value)
            self.assertIs(node.left, right)
            self.assertIs(node.right, left)

    def test_mirroring_twice_restores_structure(self):
        root = build_tree([1, 2, 3, 4, None, 5, 6, None, 7])
        before = snapshot(root)
        self.solution.mirror(root)
        self.solution.mirror(root)
        self.assertEqual(snapshot(root), before)

    def test_ten_thousand_node_chain(self):
        root = Node(1)
        node = root
        for value in range(2, 10001):
            node.left = Node(value)
            node = node.left
        self.solution.mirror(root)
        node = root
        for value in range(1, 10001):
            self.assertIsNotNone(node)
            self.assertEqual(node.data, value)
            self.assertIsNone(node.left)
            node = node.right
        self.assertIsNone(node)


if __name__ == "__main__":
    unittest.main(verbosity=2)
