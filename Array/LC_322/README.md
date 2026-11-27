# LC 322 - Coin Change

[LeetCode problem](https://leetcode.com/problems/coin-change/)

Solved: **27 November 2026**. Python 3: **Accepted, 191/191 tests**.
[Accepted submission](https://leetcode.com/problems/coin-change/submissions/2204472276/)

## Problem

With unlimited copies of each denomination, return the fewest coins needed to
form the exact amount, or -1 if impossible. There are at most 12 denominations
and the amount is between 0 and 10,000.

Examples: `[1,2,5]`, amount 11 returns 3; `[2]`, amount 3 returns -1;
`[1]`, amount 0 returns 0.

## Approach: Unbounded Knapsack

Set dp[0] = 0 and all other entries to amount + 1, an unreachable sentinel.
For each denomination, scan target values upward and relax
`dp[value] = min(dp[value], dp[value - coin] + 1)`. The smaller state may already
use this coin, so the upward order permits unlimited reuse. After processing a
coin, every combination using the denominations seen so far is represented;
induction over denominations proves dp[amount] is optimal. An unchanged
unreachable result becomes -1.

Time: O(nA). Auxiliary space: O(A), for n denominations and amount A.

Related: [LC 3946](../LC_3946/README.md) adds a one-time bonus for each activated
item type and maximizes the resulting copy count within a budget.

## Tests

```bash
python -m unittest Array.LC_322.test -v
```

Checks include examples, zero amount, impossible sums, a greedy counterexample,
maximum amount, huge denominations, and 1,000 seeded random cases checked
against breadth-first search over reachable amounts.
