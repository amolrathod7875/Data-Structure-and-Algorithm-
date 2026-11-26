from collections import Counter
from itertools import product
import random
import unittest

from Array.LC_3934.code import Solution


def oracle(nums):
    for length in range(1, len(nums) + 1):
        counts = Counter(tuple(nums[start:start + length])
                         for start in range(len(nums) - length + 1))
        if 1 in counts.values():
            return length


class UniqueSubarrayTests(unittest.TestCase):
    def test_examples(self):
        for nums, expected in [([3, 3, 3], 3), ([2, 1, 2, 3, 3], 1),
                               ([1, 1, 2, 2, 1], 2)]:
            self.assertEqual(Solution().smallestUniqueSubarray(nums), expected)

    def test_exhaustive_short_binary_arrays(self):
        for size in range(1, 10):
            for values in product([1, 2], repeat=size):
                nums = list(values)
                self.assertEqual(Solution().smallestUniqueSubarray(nums), oracle(nums), nums)

    def test_random_arrays_against_counted_subarrays(self):
        rng = random.Random(3934)
        for _ in range(1500):
            nums = [rng.randint(1, 5) for _ in range(rng.randint(1, 40))]
            original = nums[:]
            self.assertEqual(Solution().smallestUniqueSubarray(nums), oracle(nums), nums)
            self.assertEqual(nums, original)

    def test_maximum_length_patterns(self):
        for nums, expected in [([1] * 100000, 100000),
                               ([1, 2] * 50000, 99998),
                               (list(range(1, 100001)), 1),
                               ([1] * 99999 + [100000], 1)]:
            self.assertEqual(Solution().smallestUniqueSubarray(nums), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
