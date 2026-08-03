# LC 622 - Design Circular Queue

## Problem

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implement the `MyCircularQueue` class:

- `MyCircularQueue(k)` Initializes the object with the size of the queue to be `k`
- `int Front()` Gets the front item from the queue. If thequeue is empty, return `-1`
- `int Rear()` Gets the last item from the queue. If the queue is empty, return `-1`
- `boolean enQueue(int value)` Inserts an element into the circular queue. Return `true` if the operation is successful
- `boolean deQueue()` Deletes an element from the circular queue. Return `true` if the operation is successful
- `boolean isEmpty()` Checks whether the circular queue is empty or not
- `boolean isFull()` Checks whether the circular queue is full or not

**Note:** You must solve the problem without using the built-in queue data structure in your programming language.

---

## Examples

### Example 1

```
Input:
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]

Output:
[null, true, true, true, false, 3, true, true, true, 4]
```

**Explanation:**

```
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
```

---

## Approach: Array with Pointers

### Key Insight

A circular queue uses a fixed-size array and two pointers (`front` and `rear`) to track the positions. When the rear reaches the end of the array, it wraps around to the beginning using modulo arithmetic.

The key challenge is distinguishing between an **empty** queue and a **full** queue when `front == rear`. We solve this by maintaining a separate `size` counter.

### Visual Representation

```
Capacity = 3, size = 2, front = 0, rear = 2

Index:    0      1      2
Queue:  [ 1  ] [ 2 ]  [ ? ]
          ^front         ^rear

After enQueue(3):
Index:    0      1      2
Queue:  [ 1  ] [ 2 ]  [ 3 ]
          ^front         ^rear (wraps to 0)

After deQueue():
Index:    0      1      2
Queue:  [ 1  ] [ 2 ]  [ 3 ]
             ^front      ^rear
```

### Algorithm

- **enQueue(value):** If not full, place value at `rear`, advance `rear` with `(rear + 1) % capacity`, increment `size`
- **deQueue():** If not empty, advance `front` with `(front + 1) % capacity`, decrement `size`
- **Front():** Return `queue[front]` if not empty, else `-1`
- **Rear():** Return `queue[(rear - 1 + capacity) % capacity]` if not empty, else `-1`
- **isEmpty():** Return `size == 0`
- **isFull():** Return `size == capacity`

```python
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.front = 0
        self.rear = 0
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.rear - 1 + self.capacity) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
```

---

## Complexity Analysis

| Operation   | Time           | Space |
| ----------- | -------------- | ----- |
| `enQueue` | **O(1)** | O(1)  |
| `deQueue` | **O(1)** | O(1)  |
| `Front`   | **O(1)** | O(1)  |
| `Rear`    | **O(1)** | O(1)  |
| `isEmpty` | **O(1)** | O(1)  |
| `isFull`  | **O(1)** | O(1)  |

**Overall space:** O(k) for the underlying array

---

## Flowchart

```mermaid
flowchart TD
    A[enQueue value] --> B{Is queue full?}
    B -->|Yes| C[Return False]
    B -->|No| D[queue[rear] = value]
    D --> E[rear = (rear + 1) % capacity]
    E --> F[size += 1]
    F --> G[Return True]

    H[deQueue] --> I{Is queue empty?}
    I -->|Yes| J[Return False]
    I -->|No| K[front = (front + 1) % capacity]
    K --> L[size -= 1]
    L --> M[Return True]

    N[Front] --> O{Is queue empty?}
    O -->|Yes| P[Return -1]
    O -->|No| Q[Return queue[front]]

    R[Rear] --> S{Is queue empty?}
    S -->|Yes| T[Return -1]
    S -->|No| U[Return queue[(rear - 1 + capacity) % capacity]]

    V[isEmpty] --> W{size == 0?}
    W -->|Yes| X[Return True]
    W -->|No| Y[Return False]

    Z[isFull] --> AA{size == capacity?}
    AA -->|Yes| AB[Return True]
    AA -->|No| AC[Return False]
```

---

## Example Test Case Trace

**Operations:** `enQueue(1)`, `enQueue(2)`, `enQueue(3)`, `enQueue(4)`, `Rear()`, `isFull()`, `deQueue()`, `enQueue(4)`, `Rear()`

| Operation      | queue                          | front | rear | size | Action                      |
| -------------- | ------------------------------ | ----- | ---- | ---- | --------------------------- |
| `enQueue(1)` | `[1, 0, 0]`                  | 0     | 1    | 1    | queue[0]=1, rear=1          |
| `enQueue(2)` | `[1, 2, 0]`                  | 0     | 2    | 2    | queue[1]=2, rear=2          |
| `enQueue(3)` | `[1, 2, 3]`                  | 0     | 0    | 3    | queue[2]=3, rear=0 (wrap)   |
| `enQueue(4)` | `[1, 2, 3]`                  | 0     | 0    | 3    | Full, return False          |
| `Rear()`     | `[1, 2, 3]`                  | 0     | 0    | 3    | queue[(0-1+3)%3]=queue[2]=3 |
| `isFull()`   | `[1, 2, 3]`                  | 0     | 0    | 3    | size==3, return True        |
| `deQueue()`  | `[1, 2, 3]`                  | 1     | 0    | 2    | front=1, size=2             |
| `enQueue(4)` | `[1, 2, 3]` → `[4, 2, 3]` | 1     | 1    | 3    | queue[0]=4, rear=1          |
| `Rear()`     | `[4, 2, 3]`                  | 1     | 1    | 3    | queue[(1-1+3)%3]=queue[0]=4 |

---

## Run Tests

```bash
PYTHONPATH=/workspaces/Data-Structure-and-Algorithm- python Queue/LC_622/test.py
```
