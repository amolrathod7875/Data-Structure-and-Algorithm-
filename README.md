# Data-Structure-and-Algorithm-

A curated collection of Data Structure and Algorithm solutions implemented in Python.
Problems are sourced from [LeetCode (LC)](https://leetcode.com/) and [GeeksforGeeks (GFG)](https://www.geeksforgeeks.org/),
along with handwritten **Basics** implementations of core data structures.

Every problem folder contains a `code.py` (or `basics.py`) solution and a `test.py`
that exercises it.

## Repository Structure

Solutions are organized by data structure / topic. Each leaf folder is a single
problem (or a self-contained data-structure implementation):

```
<Category>/
  <Problem or Basics>/
    code.py        # solution / implementation
    test.py        # runnable tests (print-based assertions)
```

| Category | Description |
| --- | --- |
| `Array` | Array manipulation problems |
| `Doubly_Linked_List` | Doubly linked list design & basics |
| `Hash_Map` | Hash map / hashing problems |
| `Heaps` | Heap (min/max) problems & basics |
| `Math` | Math / number-theory problems |
| `Queue` | Queue, circular queue, deque & stream problems |
| `Singly_LInked_List` | Singly linked list problems |
| `Sorting` | Sorting-related problems |
| `Stack` | Stack, expression evaluation & design problems |

## How to Run

Tests import solutions as packages (`from <Category>.<Problem>.code import Solution`),
so run them from the **repository root**.

Run a single problem's tests:

```bash
python Heaps/LC_215/test.py
```

Or run all tests with pytest (installed automatically on Python 3.11+ via the
`python -m` namespace package import):

```bash
# from the repo root
python -m pytest -q
```

> Tip: if you prefer plain Python, you can run every `test.py` from the root:
> ```bash
> for f in $(find . -name test.py); do echo "== $f =="; python "$f"; done
> ```

## Problem Index

### Array

| Folder | Source | Problem |
| --- | --- | --- |
| `GFG_Kth_Largest_element` | GFG | Kth Largest Element |
| `LC_1929` | LC | Concatenation of Array |
| `LC_3701` | LC | Alternating Sum of Array |
| `LC_3925` | LC | Concatenate (Reversed) Array |
| `k largest elements in an array` | GFG | K Largest Elements in an Array |

### Doubly Linked List

| Folder | Source | Problem |
| --- | --- | --- |
| `Basics` | — | Doubly Linked List (core implementation) |
| `LC_707` | LC | Design Linked List |

### Hash Map

| Folder | Source | Problem |
| --- | --- | --- |
| `LC_1832` | LC | Check if the Sentence Is Pangram |
| `LC_217` | LC | Contains Duplicate |
| `LC_219` | LC | Contains Duplicate II |
| `LC_242` | LC | Valid Anagram |
| `LC_2657` | LC | Find the Prefix Common Array of Two Arrays |
| `LC_349` | LC | Intersection of Two Arrays |
| `LC_350` | LC | Intersection of Two Arrays II |
| `LC_3731` | LC | Find Missing Elements in Range |

### Heaps

| Folder | Source | Problem |
| --- | --- | --- |
| `Basics` | — | Min/Max Heap (core implementation) |
| `GFG_Check if an Array is Max Heap` | GFG | Check if an Array Is a Max Heap |
| `GFG_Heap_Sort` | GFG | Heap Sort |
| `GFG_Height_Of_Heap` | GFG | Height of Heap |
| `GFG_KLargest` | GFG | K Largest Elements |
| `GFG_Min_Cost_to_Connect_Ropes` | GFG | Min Cost to Connect Ropes |
| `GFG_Nearly_Sorted` | GFG | Sort a Nearly Sorted (K-Sorted) Array |
| `LC_215` | LC | Kth Largest Element in an Array |
| `LC_347` | LC | Top K Frequent Elements |

### Math

| Folder | Source | Problem |
| --- | --- | --- |
| `LC_4010` | LC | Maximum Pair Strength (gcd-based) |

### Queue

| Folder | Source | Problem |
| --- | --- | --- |
| `Basics` | — | Queue (core implementation) |
| `LC_2073` | LC | Time Needed to Buy Tickets |
| `LC_232` | LC | Implement Queue using Stacks |
| `LC_346` | LC | Moving Average from Data Stream |
| `LC_387` | LC | First Unique Character in a String |
| `LC_622` | LC | Design Circular Queue |
| `LC_641` | LC | Design Circular Deque |
| `LC_933` | LC | Number of Recent Calls |

### Singly Linked List

| Folder | Source | Problem |
| --- | --- | --- |
| `LC_92` | LC | Reverse Linked List II |

### Sorting

| Folder | Source | Problem |
| --- | --- | --- |
| `LC_1913` | LC | Maximum Product Difference Between Two Pairs |
| `LC_2037` | LC | Minimum Number of Moves to Seat Everyone |

### Stack

| Folder | Source | Problem |
| --- | --- | --- |
| `Basics` | — | Stack (core implementation) |
| `GFG_Infix Expression Evaluation` | GFG | Infix Expression Evaluation |
| `GFG_Reverse_Stack` | GFG | Reverse a Stack |
| `GFG_Sort_Stack` | GFG | Sort a Stack |
| `LC_150` | LC | Evaluate Reverse Polish Notation |
| `LC_20` | LC | Valid Parentheses |
| `LC_224` | LC | Basic Calculator |
| `LC_225` | LC | Implement Stack using Queues |
| `LC_227` | LC | Basic Calculator II |

## Stats

- **9** categories · **45** problems/data-structure implementations
- Each problem ships with a self-contained test.

---

*LC = LeetCode · GFG = GeeksforGeeks*
