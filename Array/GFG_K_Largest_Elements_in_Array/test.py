import unittest
from code import KLargest


class TestKLargest(unittest.TestCase):

    def test_basic_case(self):
        nums = [1, 23, 12, 9, 30, 2, 50]
        self.assertEqual(KLargest(nums, 3), [50, 30, 23])

    def test_k_equals_one(self):
        nums = [1, 23, 12, 9, 30, 2, 50]
        self.assertEqual(KLargest(nums, 1), [50])

    def test_k_equals_length(self):
        nums = [5, 1, 3]
        self.assertEqual(KLargest(nums, 3), [5, 3, 1])

    def test_with_duplicates(self):
        nums = [4, 4, 2, 4, 3, 1]
        self.assertEqual(KLargest(nums, 2), [4, 4])

    def test_single_element(self):
        nums = [42]
        self.assertEqual(KLargest(nums, 1), [42])

    def test_negative_numbers(self):
        nums = [-1, -3, -2, -5, 0]
        self.assertEqual(KLargest(nums, 2), [0, -1])

    def test_all_same(self):
        nums = [7, 7, 7, 7]
        self.assertEqual(KLargest(nums, 3), [7, 7, 7])

    def test_two_elements(self):
        nums = [10, 20]
        self.assertEqual(KLargest(nums, 2), [20, 10])


if __name__ == "__main__":
    unittest.main()
