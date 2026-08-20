# Basic Calculator

LeetCode 224 — Basic Calculator

## Problem

Given a string `s` which represents an arithmetic expression, implement a basic calculator to evaluate it. The expression may contain open `(` and closing parentheses `)`, the plus `+` or minus sign `-`, non-negative integers, and empty spaces.

**Examples:**
```
Input:  s = "1 + 1"
Output: 2

Input:  s = " 2-1 + 2 "
Output: 3

Input:  s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

## Constraints

- `1 <= s.length <= 3 * 10^5`
- `s` consists of digits, `+`, `-`, `(`, `)`, and ` `.
- `s` represents a valid expression.

## Approach

Use a **stack** to handle parentheses and a running evaluation:

1. Maintain `result` (current result), `sign` (current sign: +1 or -1), and `num` (current number being parsed).
2. Iterate through the string (after removing spaces):
   - If the character is a **digit**, build the number: `num = num * 10 + int(ch)`.
   - If the character is `+` or `-`:
     - Apply the current sign to the current number and add to `result`.
     - If a number was just parsed (`num > 0`), set the new sign: `+` → 1, `-` → -1.
     - If no number was parsed (`num == 0`), it's a unary operator: `+` keeps the sign, `-` flips the sign.
     - Reset `num`.
   - If the character is `(`:
     - Push the current `result` and `sign` onto the stack.
     - Reset `result` and `sign` for the sub-expression.
   - If the character is `)`:
     - Apply the current sign to the current number and add to `result`.
     - Pop the previous `sign` and `result` from the stack.
     - Multiply the current `result` by the popped `sign` and add the popped `result`.
3. After the loop, add any remaining number to the result with its sign.

## Algorithm

```python
def calculate(s: str) -> int:
    stack = []
    num = 0
    result = 0
    sign = 1
    s = s.replace(' ', '')
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '+':
            result += sign * num
            if num > 0:
                sign = 1
            num = 0
        elif ch == '-':
            result += sign * num
            if num > 0:
                sign = -1
            else:
                sign = -sign
            num = 0
        elif ch == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
            num = 0
        elif ch == ')':
            result += sign * num
            result *= stack.pop()
            result += stack.pop()
            num = 0
            sign = 1
    return result + sign * num
```

## Complexity Analysis

| Metric | Complexity |
|--------|------------|
| Time   | O(n) — single pass through the string |
| Space  | O(n) — stack space for nested parentheses |

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
- LeetCode examples
- Single number (edge case)
- Simple addition and subtraction
- Nested parentheses
- Multiple nested parentheses
- Complex expressions
- Negative inside parentheses
- Spaces in expression
- Large expressions
- Chained subtractions
- Double negative
- Complex expressions with spaces
