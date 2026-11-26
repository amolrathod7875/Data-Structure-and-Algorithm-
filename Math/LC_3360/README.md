# LC 3360 - Stone Removal Game

[LeetCode problem](https://leetcode.com/problems/stone-removal-game/)

Daily Challenge: **26 November 2026**. Python 3: **Accepted, 53/53 tests**.
[Accepted submission](https://leetcode.com/problems/stone-removal-game/submissions/2203579028/)

## Problem

Alice starts with a pile of n stones and must remove exactly 10. Bob then must
remove 9, Alice 8, and so on, always one fewer than the previous move. Whoever
cannot remove the required number loses. Determine whether Alice wins for
1 <= n <= 50.

Examples: n = 12 returns true; n = 1 returns false.

## Approach: Simulate the Forced Moves

Track the remaining stones, the next removal amount, and whose turn it is.
After every legal move, subtract the stones, reduce the required amount by one,
and switch players. When the loop stops, the current player loses, so return
the opposite of `alice_turn`.

There are no strategic choices: each move is forced. The loop therefore follows
the unique game exactly. Under n <= 50, at most seven moves are legal because
10 + 9 + 8 + 7 + 6 + 5 + 4 = 49, while the eighth requires a total of 52.
The removal amount stays positive throughout the supported input domain.

Time: O(1) for the stated constraints. Auxiliary space: O(1).

## Related Thinking

[LC 1510 - Stone Game IV](../LC_1510/README.md) also classifies whether the player
to move wins. Its players can choose among square-sized removals, so it needs
dynamic programming over winning and losing positions instead of one simulation.

## Run Tests

```bash
python -m unittest Math.LC_3360.test -v
```

Tests cover the examples, all 50 valid inputs against independently calculated
cumulative move thresholds, and both sides of every turn boundary.
