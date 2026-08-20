# LC 2037 - Minimum Number of Moves to Seat Everyone

## Problem

There are `n` available seats and `n` students standing in a room. You are given an array `seats` where `seats[i]` is the position of the `i-th` seat, and an array `students` where `students[j]` is the position of the `j-th` student.

You may perform the following move any number of times:
- Increase or decrease the position of the `i-th` student by 1 (i.e., moving from position `x` to `x + 1` or `x - 1`)

Return the **minimum number of moves** required to move each student to a seat such that no two students share the same seat.

**Note:** There may be multiple seats or students at the same position initially.

---

## Examples

### Example 1

```
Input:  seats = [3, 1, 5], students = [2, 7, 4]
Output: 4
```

**Explanation:**
- Student at position 2 → seat at position 1: 1 move
- Student at position 7 → seat at position 5: 2 moves
- Student at position 4 → seat at position 3: 1 move

Total: `1 + 2 + 1 = 4`

---

### Example 2

```
Input:  seats = [4, 1, 5, 9], students = [1, 3, 2, 6]
Output: 7
```

**Explanation:**
- Student at position 1 → seat at position 1: 0 moves
- Student at position 3 → seat at position 4: 1 move
- Student at position 2 → seat at position 5: 3 moves
- Student at position 6 → seat at position 9: 3 moves

Total: `0 + 1 + 3 + 3 = 7`

---

### Example 3

```
Input:  seats = [2, 2, 6, 6], students = [1, 3, 2, 6]
Output: 4
```

---

## Approach: Greedy + Sorting

### Key Insight

The minimum total distance is achieved when we pair the **smallest student** with the **smallest seat**, the **second smallest student** with the **second smallest seat**, and so on.

Any "crossing" assignment (e.g., pairing a leftward student with a rightward seat) creates unnecessary extra distance.

### Algorithm

1. Sort `seats` in ascending order
2. Sort `students` in ascending order
3. Pair them index-by-index and sum the absolute differences

```python
class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()

        total_moves = 0
        for seat, student in zip(seats, students):
            total_moves += abs(seat - student)

        return total_moves
```

---

## Complexity Analysis

| | Time | Space |
|--|------|-------|
| **minMovesToSeat** | **O(n log n)** — dominated by sorting both arrays | **O(n)** — for the sorted copies (or O(1) if sorting in-place) |

---

## Flowchart

```mermaid
flowchart TD
    A[Input: seats, students] --> B[Sort seats ascending]
    B --> C[Sort students ascending]
    C --> D[Initialize total_moves = 0]
    D --> E[For each pair seat[i], student[i]]
    E --> F[Add |seat[i] - student[i]| to total]
    F --> G{More pairs?}
    G -->|Yes| E
    G -->|No| H[Return total_moves]
```

---

## Example Test Case Trace

**Input:** `seats = [3, 1, 5]`, `students = [2, 7, 4]`

### Step 1: Sort both arrays

```
seats   = [3, 1, 5]   →   sorted: [1, 3, 5]
students = [2, 7, 4]   →   sorted: [2, 4, 7]
```

### Step 2: Pair and calculate moves

| Index | Seat | Student | \|Seat - Student\| |
|-------|------|---------|-------------------|
| 0     | 1    | 2       | \|1 - 2\| = **1** |
| 1     | 3    | 4       | \|3 - 4\| = **1** |
| 2     | 5    | 7       | \|5 - 7\| = **2** |

### Step 3: Sum up

```
Total moves = 1 + 1 + 2 = 4
```

---

## Run Tests

```bash
PYTHONPATH=/workspaces/Data-Structure-and-Algorithm- python Queue/LC_2037/test.py
```
