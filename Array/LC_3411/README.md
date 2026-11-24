# LC 3411 - Maximum Subarray With Equal Products

[LeetCode problem](https://leetcode.com/problems/maximum-subarray-with-equal-products/)

Daily Challenge: **24 November 2026**. Python 3: **Accepted, 865/865 tests**.
[Accepted submission](https://leetcode.com/problems/maximum-subarray-with-equal-products/submissions/2202404383/)

## Problem

Find the longest contiguous subarray whose product equals its GCD multiplied by
its LCM. The array has 2 to 100 elements, each between 1 and 10.

Examples: `[1,2,1,2,1,1,1]` returns `5`, `[2,3,4,5,6]` returns `3`, and
`[1,2,3,1,4,5,1]` returns `5`.

## Approach: Extend Every Subarray

For each left endpoint, extend the right endpoint while maintaining the product,
GCD, and LCM of the current window. Start with product 1, GCD 0, and LCM 1.
Multiplication, `gcd(current, value)`, and `lcm(current, value)` preserve the
three window aggregates after each extension. Update the maximum length whenever
the equality holds. Every nonempty contiguous subarray is checked exactly once,
so the longest valid one is found.

There are O(n²) window extensions and three scalar accumulators. GCD and LCM
remain bounded by 10 and 2520 respectively for these constraints. Python integers
keep the product exact; its bit length can grow to O(n log M), where M is the
largest element, so arithmetic and storage are not strictly constant for
unbounded inputs. With n <= 100 and M <= 10, direct enumeration is sufficient.

## Shared Thinking

This problem and [LC 1071](../../String/LC_1071/README.md) both use GCD to reason
about common factors. Here it is maintained over numeric windows; in LC 1071,
the GCD of string lengths determines the longest possible repeating block.

## Run Tests

```bash
python -m unittest Array.LC_3411.test -v
```

Tests cover all examples, maximum-length arrays, repeated prime factors,
pairwise coprime values, ones, and 1,000 seeded random arrays checked against
an oracle that independently recomputes each window's product, GCD, and LCM.
