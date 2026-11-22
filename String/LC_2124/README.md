# LC 2124 - Check if All A's Appears Before All B's

[Problem on LeetCode](https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/)

## Problem

For a string containing only `a` and `b`, determine whether all occurrences of
`a` precede all occurrences of `b`. Strings containing only one letter are valid.

| Input | Result |
| --- | --- |
| `aaabbb` | `True` |
| `abab` | `False` |
| `bbb` | `True` |

Constraints: `1 <= len(s) <= 100`; every character is `a` or `b`.

## Approach

A string fails the condition exactly when a `b` is followed immediately by an
`a`. Any `b` occurring before an `a` must eventually cross such a transition.
Check that the substring `ba` does not occur.

```python
class Solution:
    def checkString(self, s: str) -> bool:
        return "ba" not in s
```

Time: **O(n)**. Auxiliary space: **O(1)**.

## Validation

This Python 3 solution was accepted on LeetCode on 22 November 2026:
**216/216 test cases passed**.

[Accepted submission](https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/submissions/2201231832/)

Local tests cover the examples, single-character and maximum-length inputs, and
every binary string of lengths 1 through 10 against a sorted-string oracle.

Run from the repository root:

```bash
python -m String.LC_2124.test
```
