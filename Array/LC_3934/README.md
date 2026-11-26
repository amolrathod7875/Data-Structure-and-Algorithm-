# LC 3934 - Smallest Unique Subarray

[LeetCode problem](https://leetcode.com/problems/smallest-unique-subarray/)

Daily Challenge for **25 November 2026**, solved on **26 November 2026**.
Python 3: **Accepted, 719/719 tests**.
[Accepted submission](https://leetcode.com/problems/smallest-unique-subarray/submissions/2203582621/?envType=daily-question&envId=2026-11-25)

## Problem

Return the minimum length of a contiguous subarray that occurs exactly once in
the input. Identical occurrences must match in both length and corresponding
elements. The input has 1 to 100,000 elements, each between 1 and 100,000.

Examples: `[3,3,3]` returns `3`, `[2,1,2,3,3]` returns `1`, and
`[1,1,2,2,1]` returns `2`.

## Approach: Suffix Array and Adjacent Common Prefixes

Build a suffix array by repeatedly sorting suffixes by pairs of ranks for
prefixes of doubling length. A missing second half uses rank -1, so a shorter
suffix sorts before a longer suffix with the same prefix. Once all ranks are
distinct, the order is final. Kasai's algorithm then computes the longest common
prefix (LCP) of every suffix with the suffix immediately before it.

For a suffix at sorted position i, its longest prefix shared with any other
suffix has length `max(lcp[i], lcp[i+1])`, treating missing neighbors as zero.
Its shortest unique prefix therefore has length one greater, provided that
prefix fits inside the suffix. Return the minimum such length over all suffixes.

Why only neighbors? Suffixes sharing any particular prefix form a contiguous
interval in sorted order. If another suffix shares a prefix with the current
one, at least one adjacent suffix shares at least that many elements. Thus the
maximum of the two adjacent LCPs captures every possible repeated prefix.
Each subarray is a prefix of the suffix starting at its first element, so the
minimum over suffixes finds the required unique subarray.

Time: O(n log² n) worst case with comparison sorting in each doubling round,
plus O(n) for LCP construction and the final scan. Auxiliary space: O(n).
All comparisons use exact integer ranks; no probabilistic rolling hash is used.

## Run Tests

```bash
python -m unittest Array.LC_3934.test -v
```

Tests cover all examples, all 1,022 binary arrays of lengths 1 through 9,
1,500 seeded random arrays against explicit subarray frequency counts,
input preservation, and maximum-size uniform, alternating, distinct, and
unique-tail inputs.
