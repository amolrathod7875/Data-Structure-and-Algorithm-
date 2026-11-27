# LC 3946 - Maximum Number of Items From Sale I

[LeetCode problem](https://leetcode.com/problems/maximum-number-of-items-from-sale-i/)

Daily Challenge: **27 November 2026**. Python 3: **Accepted, 764/764 tests**.
[Accepted submission](https://leetcode.com/problems/maximum-number-of-items-from-sale-i/submissions/2204472092/?envType=daily-question&envId=2026-11-27)

## Problem

Each item type has a factor and price. Buy unlimited copies within a budget.
Buying the first copy of a type grants one free copy of every other type whose
factor is divisible by its factor. Extra purchases of the same type add no
further bonus. Maximize purchased plus free copies. There are at most 1,000
types; factors, prices, and budget are at most 1,500.

Examples: `[[6,2],[2,6],[3,4]]` with budget 9 returns 4;
`[[2,4],[3,2],[4,1],[6,4],[12,4]]` with budget 8 returns 10.

## Approach: First-Copy Bonus and Unlimited Extras

Count factor frequencies. For each factor f, sum the frequencies of all its
multiples. This count equals the first purchase's total gain: one purchased copy
plus all matching free types except itself. Duplicate factors are separate types.

Let dp[b] be the best total achievable within capacity b. For each type, first
scan capacities downward to add its first-copy gain at most once. Then scan
upward to allow extra copies, each adding one. A repeated-copy transition from
a state that has not activated the current type undercounts its bonus; the
first-copy transition dominates that case because the first-copy gain is at
least one. Thus it cannot produce an unattainable overestimate or omit an
optimal choice. Every legal number of copies is represented, while each type's
bonus is counted at most once. Free copies never activate additional bonuses.

Time: O(F log F + nB), where F is the largest factor and B the budget.
Auxiliary space: O(F + B). The input is unchanged.

## Related Thinking and Tests

[LC 322](../LC_322/README.md) uses the same upward capacity scan for unlimited
copies, with a minimization objective and exact target instead of bonuses.

```bash
python -m unittest Array.LC_3946.test -v
```

Checks include examples, unaffordable types, repeated factors, one-time bonuses,
the maximum-size duplicate-factor input, and 400 seeded random cases against
explicit enumeration of purchase counts and free-copy rules.
