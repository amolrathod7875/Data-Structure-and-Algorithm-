import unittest
from code import sortNearlySorted


class TestSortNearlySorted(unittest.TestCase):

    def test_k_zero_sorted(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(sortNearlySorted(arr, 0), [1, 2, 3, 4, 5])

    def test_k_one(self):
        arr = [2, 1, 4, 3, 6, 5]
        self.assertEqual(sortNearlySorted(arr, 1), [1, 2, 3, 4, 5, 6])

    def test_k_two(self):
        arr = [3, 2, 1, 6, 5, 4]
        self.assertEqual(sortNearlySorted(arr, 2), [1, 2, 3, 4, 5, 6])

    def test_gfg_example(self):
        arr = [6, 5, 3, 2, 8, 10, 9]
        self.assertEqual(sortNearlySorted(arr, 3), [2, 3, 5, 6, 8, 9, 10])

    def test_single_element(self):
        arr = [42]
        self.assertEqual(sortNearlySorted(arr, 0), [42])

    def test_with_duplicates(self):
        arr = [2, 1, 2, 1, 3, 3]
        self.assertEqual(sortNearlySorted(arr, 2), [1, 1, 2, 2, 3, 3])

    def test_negative_numbers(self):
        arr = [-3, -5, -4, -1, -2]   # each within 2 of sorted spot
        self.assertEqual(sortNearlySorted(arr, 2), [-5, -4, -3, -2, -1])

    def test_does_not_mutate_input(self):
        arr = [2, 1, 4, 3, 6, 5]
        sortNearlySorted(arr, 1)
        self.assertEqual(arr, [2, 1, 4, 3, 6, 5])


if __name__ == "__main__":
    unittest.main()
