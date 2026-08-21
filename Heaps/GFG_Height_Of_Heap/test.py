import unittest
from code import height


class TestHeightOfHeap(unittest.TestCase):

    def test_single_node(self):
        self.assertEqual(height(1), 0)

    def test_two_nodes(self):
        self.assertEqual(height(2), 1)

    def test_three_nodes(self):
        self.assertEqual(height(3), 1)

    def test_four_nodes(self):
        self.assertEqual(height(4), 2)

    def test_six_nodes(self):
        self.assertEqual(height(6), 2)

    def test_seven_nodes(self):
        self.assertEqual(height(7), 2)

    def test_eight_nodes(self):
        self.assertEqual(height(8), 3)

    def test_fifteen_nodes(self):
        self.assertEqual(height(15), 3)

    def test_sixteen_nodes(self):
        self.assertEqual(height(16), 4)

    def test_zero_nodes(self):
        # Convention: empty heap has height -1
        self.assertEqual(height(0), -1)


if __name__ == "__main__":
    unittest.main()
