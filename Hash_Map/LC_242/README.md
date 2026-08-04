# LC 242 - Valid Anagram

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **anagram** is a word formed by rearranging the letters of another word using all the original characters exactly once.

---

## Examples

### Example 1

```
Input:  s = "anagram", t = "nagaram"
Output: true
```

---

### Example 2

```
Input:  s = "rat", t = "car"
Output: false
```

---

## Approach: Hash Map (Character Frequency Counter)

### Key Insight

Two strings are anagrams if and only if they have **exactly the same character counts**. We can verify this by:

1. Counting how many times each character appears in `s`
2. Decrementing those counts as we scan `t`
3. If we ever try to decrement a character that doesn't exist, or a count goes negative, they're not anagrams

### Algorithm

1. If `len(s) != len(t)`, return `False` immediately
2. Build a frequency hash map for `s`
3. Scan `t` and decrement counts
4. If any count drops below 0, return `False`
5. Return `True`

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False

        return True
```

---

## Complexity Analysis

| | Time | Space |
|--|------|-------|
| **isAnagram** | **O(n)** — two passes through the strings | **O(1)** — at most 26 lowercase letters stored |

---

## Flowchart

```mermaid
flowchart TD
    A[Input: strings s, t] --> B{len(s) == len(t)?}
    B -->|No| C[Return False]
    B -->|Yes| D[Build frequency map from s]
    D --> E[For each ch in t]
    E --> F{ch in map?}
    F -->|No| C
    F -->|Yes| G[map[ch] -= 1]
    G --> H{map[ch] < 0?}
    H -->|Yes| C
    H -->|No| I{More chars in t?}
    I -->|Yes| E
    I -->|No| J[Return True]
```

---

## Example Test Case Trace

**Input:** `s = "anagram"`, `t = "nagaram"`

### Step 1: Build frequency map from `s`

| Character | Count |
|-----------|-------|
| a | 3 |
| n | 1 |
| g | 1 |
| r | 1 |
| m | 1 |

### Step 2: Scan `t` and decrement

| Character | Action | Count after |
|-----------|--------|-------------|
| n | decrement n | n: 0 |
| a | decrement a | a: 2 |
| g | decrement g | g: 0 |
| a | decrement a | a: 1 |
| r | decrement r | r: 0 |
| a | decrement a | a: 0 |
| m | decrement m | m: 0 |

All counts end at 0, no negatives → **Return True**

---

## Run Tests

```bash
PYTHONPATH=/workspaces/Data-Structure-and-Algorithm- python Hash_Map/LC_242/test.py
```
