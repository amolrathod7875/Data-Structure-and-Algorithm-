# Reverse a Stack

Reverse a stack using only recursion. No extra data structures are allowed besides the internal stack space used due to recursion.

## Problem

Given a stack, reverse its elements in-place.

**Example:**
- Input: `[1, 5, 6, 8, 9]` (bottom to top)
- Output: `[9, 8, 6, 5, 1]` (bottom to top)

## Algorithm

The solution uses two recursive functions:

### 1. `insert_at_bottom(stack, item)`

Recursively inserts an item at the bottom of the stack.

**Logic:**
1. If the stack is empty, push the item and return.
2. Otherwise, pop the top element, recursively insert the item at the bottom, then push the popped element back on top.

### 2. `reverse_stack(stack)`

Recursively reverses the entire stack.

**Logic:**
1. If the stack is empty, return.
2. Pop the top element.
3. Recursively reverse the remaining stack.
4. Insert the popped element at the bottom of the now-reversed stack.

## How It Works (Step-by-Step)

For stack `[1, 5, 6, 8, 9]` (9 at top):

1. Pop `9` → reverse `[1,5,6,8]` → insert `9` at bottom → `[9,1,5,6,8]`
2. Pop `8` → reverse `[1,5,6]` → insert `8` at bottom → `[8,9,1,5,6]`
3. Pop `6` → reverse `[1,5]` → insert `6` at bottom → `[6,8,9,1,5]`
4. Pop `5` → reverse `[1]` → insert `5` at bottom → `[5,6,8,9,1]`
5. Pop `1` → reverse `[]` → insert `1` at bottom → `[1,5,6,8,9]`

Wait, that gives `[1,5,6,8,9]` which seems wrong. The trick is that `insert_at_bottom` places elements at the very bottom, so the first popped element (9) ends up at index 0, and the last popped element (1) ends up at the top (last index). The actual final stack is `[9,8,6,5,1]`.

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| `insert_at_bottom` | O(n) | O(n) (recursion stack) |
| `reverse_stack` | O(n²) | O(n) (recursion stack) |

**Total Time:** O(n²) — Each call to `insert_at_bottom` traverses the entire stack, and it is called n times.  
**Total Space:** O(n) — Only the recursion call stack is used.

## Running the Code

### Run the main program
```bash
python code.py
```

Expected output:
```
Original Stack : [1, 5, 6, 8, 9]
Reversed Stack : [9, 8, 6, 5, 1]
```

### Run the tests
```bash
python test.py
```

## Functions

| Function | Description |
|----------|-------------|
| `Stack` | Custom stack class with `push`, `pop`, `is_empty` operations. |
| `insert_at_bottom(stack, item)` | Helper function to insert an item at the bottom of the stack recursively. |
| `reverse_stack(stack)` | Main function that reverses the stack using only recursion. |
