from itertools import product
import random
import unittest

from String.LC_1071.code import Solution


def oracle(first, second):
    for size in range(min(len(first), len(second)), 0, -1):
        candidate = first[:size]
        if (len(first) % size == 0 and len(second) % size == 0
                and candidate * (len(first) // size) == first
                and candidate * (len(second) // size) == second):
            return candidate
    return ''


class GCDStringsTests(unittest.TestCase):
    def test_examples(self):
        for first, second, expected in [
            ('ABCABC', 'ABC', 'ABC'), ('ABABAB', 'ABAB', 'AB'),
            ('LEET', 'CODE', ''), ('AAAAAB', 'AAA', ''),
        ]:
            self.assertEqual(Solution().gcdOfStrings(first, second), expected)

    def test_boundaries(self):
        for first, second, expected in [
            ('A', 'A', 'A'), ('A' * 1000, 'A' * 999, 'A'),
            ('AB' * 500, 'AB' * 250, 'AB' * 250),
            ('AB', 'BA', ''), ('ABC', 'ABC', 'ABC'),
        ]:
            self.assertEqual(Solution().gcdOfStrings(first, second), expected)

    def test_exhaustive_short_binary_strings(self):
        strings = [''.join(chars) for size in range(1, 5)
                   for chars in product('AB', repeat=size)]
        for first in strings:
            for second in strings:
                self.assertEqual(Solution().gcdOfStrings(first, second),
                                 oracle(first, second), (first, second))

    def test_random_repetitions_and_mismatches(self):
        rng = random.Random(1071)
        for _ in range(1000):
            base = ''.join(rng.choices('ABC', k=rng.randint(1, 8)))
            first = base * rng.randint(1, 12)
            second = base * rng.randint(1, 12)
            if rng.choice([False, True]):
                second += 'Z'
            self.assertEqual(Solution().gcdOfStrings(first, second),
                             oracle(first, second))


if __name__ == '__main__':
    unittest.main(verbosity=2)
