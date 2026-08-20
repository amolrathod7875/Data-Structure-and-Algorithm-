import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from code import Stack, reverse_stack


class TestReverseStack(unittest.TestCase):
    
    def test_reverse_basic(self):
        st = Stack()
        for val in [1, 5, 6, 8, 9]:
            st.push(val)
        reverse_stack(st)
        self.assertEqual(st.stack, [9, 8, 6, 5, 1])

    def test_reverse_two_elements(self):
        st = Stack()
        for val in [1, 2]:
            st.push(val)
        reverse_stack(st)
        self.assertEqual(st.stack, [2, 1])

    def test_reverse_single_element(self):
        st = Stack()
        st.push(42)
        reverse_stack(st)
        self.assertEqual(st.stack, [42])

    def test_reverse_empty_stack(self):
        st = Stack()
        reverse_stack(st)
        self.assertTrue(st.is_empty())
        self.assertEqual(st.stack, [])

    def test_reverse_three_elements(self):
        st = Stack()
        for val in [3, 2, 1]:
            st.push(val)
        reverse_stack(st)
        self.assertEqual(st.stack, [1, 2, 3])

    def test_reverse_preserves_all_elements(self):
        original = [10, 20, 30, 40, 50]
        st = Stack()
        for val in original:
            st.push(val)
        reverse_stack(st)
        self.assertEqual(sorted(st.stack), sorted(original))


if __name__ == "__main__":
    unittest.main()
