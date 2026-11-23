from math import prod
import random
import unittest

from Array.LC_1352.code import ProductOfNumbers


class ProductTests(unittest.TestCase):
    def test_example(self):
        stream = ProductOfNumbers()
        for value in [3, 0, 2, 5, 4]:
            stream.add(value)
        self.assertEqual([stream.getProduct(k) for k in (2, 3, 4)], [20, 40, 0])
        stream.add(8)
        self.assertEqual(stream.getProduct(2), 32)

    def test_zero_boundaries(self):
        stream = ProductOfNumbers()
        for value in [7, 0, 0, 2, 3]:
            stream.add(value)
        self.assertEqual(stream.getProduct(1), 3)
        self.assertEqual(stream.getProduct(2), 6)
        self.assertEqual(stream.getProduct(3), 0)
        self.assertEqual(stream.getProduct(5), 0)
        stream.add(0)
        self.assertEqual(stream.getProduct(1), 0)

    def test_full_nonzero_suffix_and_repeated_queries(self):
        stream = ProductOfNumbers()
        for value in [1, 100, 1, 2]:
            stream.add(value)
        for _ in range(5):
            self.assertEqual(stream.getProduct(4), 200)
            self.assertEqual(stream.getProduct(1), 2)

    def test_operation_limit(self):
        stream = ProductOfNumbers()
        for _ in range(39999):
            stream.add(1)
        self.assertEqual(stream.getProduct(39999), 1)

    def test_random_streams_against_direct_product(self):
        rng = random.Random(1352)
        for _ in range(100):
            stream = ProductOfNumbers()
            values = []
            for _ in range(100):
                value = rng.randint(0, 5)
                if value and prod(values[-9:] + [value]) >= 2**31:
                    value = 0
                values.append(value)
                stream.add(value)
                k = rng.randint(1, len(values))
                self.assertEqual(stream.getProduct(k), prod(values[-k:]))


if __name__ == '__main__':
    unittest.main(verbosity=2)
