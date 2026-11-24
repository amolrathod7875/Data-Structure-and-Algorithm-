from math import gcd, lcm, prod
import random
import unittest

from Array.LC_3411.code import Solution


def oracle(nums):
    best = 0
    for left in range(len(nums)):
        for right in range(left + 1, len(nums) + 1):
            window = nums[left:right]
            if prod(window) == gcd(*window) * lcm(*window):
                best = max(best, len(window))
    return best


class MaximumLengthTests(unittest.TestCase):
    def test_examples(self):
        for nums, expected in [
            ([1, 2, 1, 2, 1, 1, 1], 5),
            ([2, 3, 4, 5, 6], 3),
            ([1, 2, 3, 1, 4, 5, 1], 5),
        ]:
            self.assertEqual(Solution().maxLength(nums), expected)

    def test_boundaries_and_prime_overlap(self):
        for nums, expected in [
            ([1] * 100, 100), ([10] * 100, 2),
            ([2, 3, 5, 7], 4), ([2, 4], 2), ([1, 1], 2),
            ([6, 10, 15], 2), ([1, 1, 2, 1, 1], 5),
        ]:
            self.assertEqual(Solution().maxLength(nums), expected)

    def test_random_arrays_against_recomputed_windows(self):
        rng = random.Random(3411)
        for _ in range(1000):
            nums = [rng.randint(1, 10) for _ in range(rng.randint(2, 12))]
            before = nums[:]
            self.assertEqual(Solution().maxLength(nums), oracle(nums), nums)
            self.assertEqual(nums, before)


if __name__ == '__main__':
    unittest.main(verbosity=2)
