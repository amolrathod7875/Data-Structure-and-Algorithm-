import unittest
from code import findkthlargest


class TestFindKthLargest(unittest.TestCase):

    def test_basic_case(self):
        nums = [3, 2, 1, 5, 6, 4]
        self.assertEqual(findkthlargest(nums, 2), 5)

    def test_k_equals_one(self):
        nums = [3, 2, 1, 5, 6, 4]
        self.assertEqual(findkthlargest(nums, 1), 6)

    def test_k_equals_length(self):
        nums = [3, 2, 1, 5, 6, 4]
        self.assertEqual(findkthlargest(nums, 6), 1)

    def test_with_duplicates(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        self.assertEqual(findkthlargest(nums, 4), 4)

    def test_single_element(self):
        nums = [42]
        self.assertEqual(findkthlargest(nums, 1), 42)

    def test_negative_numbers(self):
        nums = [-1, -3, -2, -5, 0]
        self.assertEqual(findkthlargest(nums, 2), -1)

    def test_two_elements(self):
        nums = [5, 1]
        self.assertEqual(findkthlargest(nums, 1), 5)
        self.assertEqual(findkthlargest(nums, 2), 1)

    def test_all_same(self):
        nums = [7, 7, 7, 7]
        self.assertEqual(findkthlargest(nums, 3), 7)


if __name__ == "__main__":
    unittest.main()
