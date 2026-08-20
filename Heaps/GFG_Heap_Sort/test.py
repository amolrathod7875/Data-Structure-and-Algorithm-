import unittest
from code import heapSort


class TestHeapSort(unittest.TestCase):

    def test_basic_case(self):
        arr = [12, 11, 13, 5, 6, 7]
        heapSort(arr)
        self.assertEqual(arr, [5, 6, 7, 11, 12, 13])

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        heapSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        heapSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_with_duplicates(self):
        arr = [4, 2, 4, 3, 2, 1]
        heapSort(arr)
        self.assertEqual(arr, [1, 2, 2, 3, 4, 4])

    def test_single_element(self):
        arr = [42]
        heapSort(arr)
        self.assertEqual(arr, [42])

    def test_empty_array(self):
        arr = []
        heapSort(arr)
        self.assertEqual(arr, [])

    def test_negative_numbers(self):
        arr = [-3, -1, -2, -5, 0]
        heapSort(arr)
        self.assertEqual(arr, [-5, -3, -2, -1, 0])

    def test_large_random_like(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        heapSort(arr)
        self.assertEqual(arr, [11, 12, 22, 25, 34, 64, 90])


if __name__ == "__main__":
    unittest.main()
