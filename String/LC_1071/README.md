# LC 1071 - Greatest Common Divisor of Strings

[LeetCode problem](https://leetcode.com/problems/greatest-common-divisor-of-strings/)

Solved: **24 November 2026**. Python 3: **Accepted, 129/129 tests**.
[Accepted submission](https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/2202406248/)

## Problem

Return the longest string that can be repeated to produce both input strings,
or the empty string if no such block exists. Both strings contain uppercase
English letters and have lengths between 1 and 1,000.

Examples: `ABCABC` and `ABC` return `ABC`; `ABABAB` and `ABAB` return `AB`;
`LEET` and `CODE` return the empty string.

## Approach: Compatible Repetitions and GCD

If both strings repeat a common block, concatenating them in either order gives
the same result. If `str1 + str2 != str2 + str1`, return the empty string.
Otherwise the strings share a repeating base, and a common divisor's length
must divide both input lengths. The largest valid length is their numeric GCD,
so return that many characters from the beginning of `str1`.

Time: O(m + n), dominated by concatenation and comparison. Auxiliary space:
O(m + n) for the concatenated strings; the returned prefix uses O(gcd(m, n)) space.

Related concept: [LC 3411](../../Array/LC_3411/README.md) uses GCD alongside LCM
and products while enumerating numeric subarrays.

## Run Tests

```bash
python -m unittest String.LC_1071.test -v
```

Tests cover the examples, single-character and maximum-length inputs, identical
strings, incompatible ordering, all 900 pairs of nonempty binary strings up to
length four, and 1,000 seeded random repetition/mismatch cases. The oracle tries
candidate prefixes directly rather than using the concatenation/GCD shortcut.
