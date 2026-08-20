# Basic Calculator II

LeetCode 227 — Basic Calculator II

## Problem

Given a string `s` which represents an arithmetic expression, implement a basic calculator to evaluate it. The expression contains only non-negative integers, the operators `+`, `-`, `*`, `/`, and empty spaces. Integer division should truncate toward zero.

**Examples:**
```
Input:  s = "3+2*2"
Output: 7

Input:  s = " 3/2 "
Output: 1

Input:  s = " 3+5 / 2 "
Output: 5
```

## Constraints

- `1 <= s.length <= 3 * 10^5`
- `s` consists of integers and operators (`+`, `-`, `*`, `/`) separated by some number of spaces.
- All the integers in the expression are non-negative integers in the range `[0, 2^31 - 1]`.
- The answer is guaranteed to fit in a 32-bit signed integer.

## Approach

Use a **stack** to handle operator precedence:

1. Iterate through the string, parsing numbers digit by digit.
2. When an operator is encountered (or at the end of the string), apply the **previous operator** to the current number:
   - `+` → push the number onto the stack.
   - `-` → push `-number` onto the stack.
   - `*` → pop the top of the stack, multiply by the number, and push the result.
   - `/` → pop the top of the stack, divide by the number (truncate toward zero), and push the result.
3. Update the current operator and reset the number.
4. After the loop, return the sum of the stack.

This approach naturally handles precedence because `*` and `/` are applied immediately to the previous number, while `+` and `-` defer their effect by storing signed values.

## Algorithm

```python
def calculate(s: str) -> int:
    stack = []
    num = 0
    op = '+'
    s = s.replace(' ', '')
    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num * 10 + int(ch)
        if ch in '+-*/' or i == len(s) - 1:
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack.append(stack.pop() * num)
            else:
                prev = stack.pop()
                stack.append(int(prev / num))
            op = ch
            num = 0
    return sum(stack)
```

## Complexity Analysis

| Metric | Complexity |
|--------|------------|
| Time   | O(n) — single pass through the string |
| Space  | O(n) — stack space for intermediate values |

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
- Each operator individually (addition, subtraction, multiplication, division)
- Mixed operators respecting precedence
- Division truncation toward zero (positive and negative)
- Spaces in expression
- Large numbers
- Zero operands
- Negative results
