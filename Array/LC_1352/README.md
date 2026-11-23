# LC 1352 - Product of the Last K Numbers

[LeetCode problem](https://leetcode.com/problems/product-of-the-last-k-numbers/)

Daily Challenge: **23 November 2026**. Python 3: **Accepted, 35/35 tests**.
[Accepted submission](https://leetcode.com/problems/product-of-the-last-k-numbers/submissions/2201982385/)

## Problem

Maintain an integer stream with `add(num)` and return the product of its last
`k` numbers using `getProduct(k)`. Queries always have enough preceding numbers.
There are at most 40,000 operations, with numbers from 0 to 100. Products of
contiguous sequences fit in a 32-bit integer.

Example: after adding `[3, 0, 2, 5, 4]`, products for the last 2, 3, and 4
numbers are `20`, `40`, and `0`. Adding `8` makes the last-2 product `32`.

## Approach: Prefix Products Since the Last Zero

Store cumulative products starting with the sentinel `1`. A nonzero addition
extends this list. A zero resets it to `[1]`, because every query crossing that
zero must return zero. Otherwise divide the newest prefix product by the prefix
immediately before the requested suffix.

Invariant: `prefix[i]` is the product of the first `i` values after the latest
zero. If `k >= len(prefix)`, the suffix includes a zero. Otherwise the division
`prefix[-1] // prefix[-k-1]` cancels all earlier factors exactly.

| Operation | Time | Auxiliary storage |
| --- | --- | --- |
| `add` | O(1) amortized | O(n) total |
| `getProduct` | O(1) | O(1) |

The amortized bound accounts for list growth and discarding prefixes on zero.

## Run Tests

```bash
python -m unittest Array.LC_1352.test -v
```

Tests cover the example, zero boundaries, consecutive zeros, repeated queries,
40,000 operations, and random operation sequences checked against direct products.
