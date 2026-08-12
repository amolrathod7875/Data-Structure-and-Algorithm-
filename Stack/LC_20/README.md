# Valid Parentheses

LeetCode 20 — Valid Parentheses

## Problem

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

Open brackets must be closed by the same type of brackets, and open brackets must be closed in the correct order.

**Examples:**
```
Input:  s = "()"
Output: true

Input:  s = "()[]{}"
Output: true

Input:  s = "(]"
Output: false

Input:  s = "([)]"
Output: false

Input:  s = "{[]}"
Output: true
```

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`

## Approach

Use a **stack** to track opening brackets. For each character:
1. If it's an **opening bracket** (`(`, `[`, `{`), push it onto the stack.
2. If it's a **closing bracket** (`)`, `]`, `}`):
   - If the stack is empty, return `False` (no matching opening bracket).
   - Check if the top of the stack matches the corresponding opening bracket.
   - If it doesn't match, return `False`.
   - If it matches, pop the stack.
3. After processing all characters, if the stack is empty, return `True`; otherwise, return `False`.

## Algorithm

```python
def isValid(s: str) -> bool:
    stack = []
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            top = stack[-1]
            if (char == ')' and top != '(') or \
               (char == ']' and top != '[') or \
               (char == '}' and top != '{'):
                return False
            stack.pop()
    return not stack
```

## Complexity Analysis

| Metric | Complexity |
|--------|------------|
| Time   | O(n) — single pass through the string |
| Space  | O(n) — stack space for storing opening brackets |

## Running the Code

### Run the main program
```bash
python code.py
```

### Run the tests
```bash
python test.py
```

## Test Cases

The test suite covers:
- Simple valid and invalid cases (`()`, `(]`)
- All bracket types (`()[]{}`, `([)]`)
- Nested brackets (`{[]}`, `({[]})`)
- Edge cases: empty string, single bracket, only opening/closing
- Mismatched nesting
- Multiple same-type brackets (`((()))`)
- Extra opening or closing brackets
