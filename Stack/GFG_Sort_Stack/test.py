import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from code import Stack, SortedInsert, SortStack


class TestSortStack(unittest.TestCase):
    
    def test_sort_basic(self):
        st = Stack()
        for val in [41, 3, 32, 2, 11]:
            st.push(val)
        SortStack(st.stack)
        self.assertEqual(st.stack, [2, 3, 11, 32, 41])

    def test_sort_single_element(self):
        st = Stack()
        st.push(5)
        SortStack(st.stack)
        self.assertEqual(st.stack, [5])

    def test_sort_empty_stack(self):
        st = Stack()
        SortStack(st.stack)
        self.assertEqual(st.stack, [])

    def test_sort_already_sorted(self):
        st = Stack()
        for val in [1, 2, 3, 4, 5]:
            st.push(val)
        SortStack(st.stack)
        self.assertEqual(st.stack, [1, 2, 3, 4, 5])

    def test_sort_reverse_sorted(self):
        st = Stack()
        for val in [5, 4, 3, 2, 1]:
            st.push(val)
        SortStack(st.stack)
        self.assertEqual(st.stack, [1, 2, 3, 4, 5])

    def test_sorted_insert_into_empty(self):
        st = []
        SortedInsert(st, 10)
        self.assertEqual(st, [10])

    def test_sorted_insert_smaller_than_top(self):
        st = [1, 3, 5]
        SortedInsert(st, 2)
        self.assertEqual(st, [1, 2, 3, 5])

    def test_sorted_insert_larger_than_top(self):
        st = [1, 3, 5]
        SortedInsert(st, 7)
        self.assertEqual(st, [1, 3, 5, 7])

    def test_sorted_insert_duplicate(self):
        st = [1, 3, 5]
        SortedInsert(st, 3)
        self.assertEqual(st, [1, 3, 3, 5])


if __name__ == "__main__":
    unittest.main()
