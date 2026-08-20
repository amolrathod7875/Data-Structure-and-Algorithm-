# Evaluate Reverse Polish Notation

LeetCode 150 — Evaluate Reverse Polish Notation

## Problem

You are given an array of strings `tokens` that represents an arithmetic expression in Reverse Polish Notation (RPN).

Evaluate the expression and return the resulting integer.

**Examples:**
```
Input:  tokens = ["2","1","+","3","*"]
Output: 9

Input:  tokens = ["4","13","5","/","+"]
Output: 6

Input:  tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
```

## Constraints

- `1 <= tokens.length <= 10^4`
- `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`
- Division between two integers should truncate toward zero.

## Approach

Use a **stack** to evaluate the RPN expression:
1. Iterate through each token.
2. If the token is an **operand**, push it onto the stack.
3. If the token is an **operator**:
   - Pop the **right operand** (second operand).
   - Pop the **left operand** (first operand).
   - Apply the operator.
   - Push the result back onto the stack.
4. After processing all tokens, the stack contains exactly one element, which is the result.

For division, use `int(left / right)` to ensure truncation toward zero (e.g., `-3 / 2 = -1.5`, truncated to `-1`).

## Algorithm

```python
def evalRPN(tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if token in "+-*/":
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            else:
                result = int(left / right)
            stack.append(result)
        else:
            stack.append(int(token))
    return stack[-1]
```

## Complexity Analysis

| Metric | Complexity |
|--------|------------|
| Time   | O(n) — single pass through the tokens |
| Space  | O(n) — stack space for intermediate operands |

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
- Negative numbers
- Division truncation toward zero
- Each operator individually
- Chained operations
- Complex expressions with all operators
- Zero operands
