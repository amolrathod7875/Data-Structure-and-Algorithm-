# GFG Infix Expression Evaluation

Evaluate arithmetic expressions given in **infix notation** using two stacks.

## Algorithm

This implementation uses the classic **Two-Stack Algorithm** (based on Dijkstra's Shunting Yard algorithm):

1. **Values Stack**: Stores numeric operands.
2. **Operators Stack**: Stores operators (`+`, `-`, `*`, `/`, `^`) and parentheses.

### Processing Logic

- **Number**: Push directly onto the values stack.
- **Operator**:
  - While the top of the operators stack has **higher precedence** than the current token, **or** equal precedence and the current operator is **left-associative**:
    - Pop two values and one operator.
    - Apply the operation.
    - Push the result back onto the values stack.
  - Push the current operator onto the operators stack.
- **Parentheses** (`(`, `)`): Supported when passed as separate tokens in the input array.

### Precedence & Associativity

| Operator | Precedence | Associativity |
|----------|-----------|---------------|
| `^`      | 3         | Right         |
| `*`, `/` | 2         | Left          |
| `+`, `-` | 1         | Left          |

**Right-associative** (`^`): `a ^ b ^ c` is evaluated as `a ^ (b ^ c)`.  
**Left-associative** (`+`, `-`, `*`, `/`): `a - b - c` is evaluated as `(a - b) - c`.

## Complexity

- **Time Complexity**: `O(N)` — Each token is pushed and popped at most once from each stack.
- **Space Complexity**: `O(N)` — In the worst case, both stacks store up to `N` elements.

## Files

- `code.py` — Core evaluation logic.
- `test.py` — Unit tests covering basic operations, precedence, associativity, parentheses, and negative numbers.

## How to Run

```bash
# Run the main example
python code.py

# Run the test suite
python test.py