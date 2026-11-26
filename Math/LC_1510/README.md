# LC 1510 - Stone Game IV

[LeetCode problem](https://leetcode.com/problems/stone-game-iv/)

Solved: **26 November 2026**. Python 3: **Accepted, 72/72 tests**.
[Accepted submission](https://leetcode.com/problems/stone-game-iv/submissions/2203579713/)

## Problem

Alice and Bob take turns removing any positive perfect-square number of stones
from a pile. Alice starts, both play optimally, and a player unable to move loses.
Return whether Alice wins for 1 <= n <= 100,000.

Examples: n = 1 returns true, n = 2 returns false, and n = 4 returns true.

## Approach: Winning and Losing States

Let `winning[s]` mean that the player to move with s stones can force a win.
The empty pile is losing. Process pile sizes in increasing order and try each
square-sized removal. A state wins if at least one legal move leaves a losing
state for the opponent; otherwise it loses.

All transitions reach smaller states, which are already finalized. By induction,
each recorded state therefore matches optimal play. `winning[n]` describes
Alice's starting position. A bytearray stores the flags compactly, and early exit
avoids checking further removals after a winning move is found.

Time: O(n sqrt(n)) worst case. Auxiliary space: O(n), including the flags and
O(sqrt(n)) precomputed squares. No recursive stack is required.

## Related Thinking

[LC 3360 - Stone Removal Game](../LC_3360/README.md) has forced moves and can be
simulated directly. The shared idea is identifying the player who eventually
faces a losing position; this problem adds strategic choices.

## Run Tests

```bash
python -m unittest Math.LC_1510.test -v
```

Tests cover examples, known losing positions, all pile sizes 1 through 200
against recursive minimax, perfect squares, and near-maximum inputs against
an independent oracle that propagates winning positions forward from losing ones.
