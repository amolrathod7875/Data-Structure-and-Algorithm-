# Sort a Stack

Sort a stack using only recursion. No extra data structures are allowed besides the internal stack space used due to recursion.

## Problem

Given a stack, sort its elements in ascending order (smallest element at the bottom, largest at the top).

**Example:**
- Input: `[41, 3, 32, 2, 11]` (bottom to top)
- Output: `[2, 3, 11, 32, 41]` (bottom to top)

## Algorithm

The solution uses two recursive functions:

### 1. `SortedInsert(st, x)`

Inserts element `x` into a stack `st` that is already sorted in ascending order.

**Logic:**
1. If the stack is empty OR the top element is less than or equal to `x`, push `x` and return.
2. Otherwise, pop the top element, recursively insert `x`, then push the popped element back on top.

### 2. `SortStack(st)`

Sorts the entire stack using recursion.

**Logic:**
1. If the stack is empty, return.
2. Pop the top element.
3. Recursively sort the remaining stack.
4. Insert the popped element into the sorted stack using `SortedInsert`.

## How It Works (Step-by-Step)

For stack `[41, 3, 32, 2, 11]` (11 at top):

1. Pop `11` → sort `[41, 3, 32, 2]` → insert `11` → results in sorted stack with 11 inserted
2. Pop `2` → sort remaining → insert `2` at correct position
3. Continue until all elements are inserted in sorted order

The final stack (bottom to top): `[2, 3, 11, 32, 41]`

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| `SortedInsert` | O(n) | O(n) (recursion stack) |
| `SortStack` | O(n²) | O(n) (recursion stack) |

**Total Time:** O(n²) — Each call to `SortedInsert` may traverse the entire stack, and it is called n times.  
**Total Space:** O(n) — Only the recursion call stack is used.

## Running the Code

### Run the main program
```bash
python code.py
```

Expected output:
```
Original Stack :  [41, 3, 32, 2, 11]
Sorted Stack : [2, 3, 11, 32, 41]
```

### Run the tests
```bash
python test.py
```

## Functions

| Function | Description |
|----------|-------------|
| `Stack` | Custom stack class with `push`, `pop`, `is_empty` operations. |
| `SortedInsert(st, x)` | Helper function to insert an element into a sorted stack while maintaining sorted order. |
| `SortStack(st)` | Main function that sorts the stack using only recursion. |
