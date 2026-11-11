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
| `Searching` | Searching & binary search problems |
| `Singly_LInked_List` | Singly linked list problems |
| `Sorting` | Sorting-related problems |
| `Stack` | Stack, expression evaluation & design problems |

## How to Run

Tests import solutions as packages (`from <Category>.<Problem>.code import Solution`),
so run them from the **repository root** with `-m`, which puts the root on `sys.path`:

```bash
python -m Heaps.LC_215.test
```

Folders written in the `unittest` style (`from code import ...`) import their sibling
module by name, so they are run from their own folder:

```bash
cd Array/GFG_Kth_Largest_element && python test.py
```

Both styles can also be run from the repository root with `PYTHONPATH`:

```bash
PYTHONPATH=. python Heaps/LC_215/test.py
```

> Tip: to run every `test.py` from the root:
> ```bash
> for f in $(find . -name test.py); do echo "== $f =="; PYTHONPATH=. python "$f"; done
> ```

## Problem Index

### Array

| Folder | Source | Problem |
| --- | --- | --- |
| `GFG_Kth_Largest_element` | GFG | Kth Largest Element |
| `GFG_Replace_0s_With_5` | GFG | Replace All 0's With 5 |
| `LC_189` | LC | Rotate Array (3 reversals / slicing) |
| `LC_215` | LC | Kth Largest Element in an Array |
| `LC_1929` | LC | Concatenation of Array |
| `LC_1877` | LC | Minimize Maximum Pair Sum in Array |
| `LC_3701` | LC | Alternating Sum of Array |
| `LC_2460` | LC | Apply Operations to an Array |
| `LC_283` | LC | Move Zeroes |
| `GFG_Move_All_Zeroes_to_End` | GFG | Move All Zeroes to End |
| `LC_3925` | LC | Concatenate (Reversed) Array |
| `LC_3194` | LC | Minimum Average of Smallest and Largest Elements |
| `GFG_Array_Of_Pairs` | GFG | Array of Pairs |
| `GFG_Check_Identical_Arrays` | GFG | Check Identical Arrays |
| `GFG_End_Insert` | GFG | Insert at End of Array |
| `GFG_Elements_Less_Than_K` | GFG | Elements Less Than K |
| `GFG_Get_Smaller` | GFG | Get Smaller in Array |
| `GFG_Reverse_Array` | GFG | Reverse Array |
| `GFG_Rotate_Array_By_One` | GFG | Rotate Array by One |
| `GFG_Second_Largest` | GFG | Second Largest |
| `GFG_Smallest_in_Array` | GFG | Smallest in Array |
| `GFG_Sum_of_Array` | GFG | Sum of Array |
| `GFG_K_Largest_Elements_in_Array` | GFG | K Largest Elements in an Array |

| GFG_Alternates_in_Array | GFG | Alternates in Array |
| GFG_Array_Traversal | GFG | Array Traversal |
| GFG_Ceil_in_Sorted_Array | GFG | Ceil in Sorted Array |
| GFG_Count_Occurrences_in_Sorted | GFG | Count Occurrences in Sorted Array |
| GFG_Insert_Interval | GFG | Insert Interval |
| GFG_Kadanes_Algorithm | GFG | Kadane's Algorithm |
| GFG_Merge_Without_Extra_Space | GFG | Merge Without Extra Space |
| GFG_Minimize_the_Heights | GFG | Minimize the Heights |
| GFG_Next_Permutation | GFG | Next Permutation |
| GFG_Non_Overlapping_Intervals | GFG | Non-Overlapping Intervals |
| GFG_Overlapping_Intervals | GFG | Overlapping Intervals |
| GFG_Smallest_Positive_Missing | GFG | Smallest Positive Missing |
| GFG_Stock_Buy_and_Sell_Max_One_Transaction | GFG | Stock Buy and Sell - Max One Transaction |
| GFG_Stock_Buy_and_Sell_Multiple_Transaction | GFG | Stock Buy and Sell - Multiple Transactions |
| LC_56 | LC | Merge Intervals |
| LC_1011 | LC | Capacity To Ship Packages Within D Days |
| LC_1288 | LC | Remove Covered Intervals |
| LC_1470 | LC | Shuffle the Array |
| LC_1480 | LC | Running Sum of 1d Array |

### Doubly Linked List

| Folder | Source | Problem |
| --- | --- | --- |
| `Basics` | — | Doubly Linked List (core implementation) |
| `LC_707` | LC | Design Linked List |

### Hash Map

| Folder | Source | Problem |
| --- | --- | --- |
| `GFG_Majority_Element_More_Than_n_3` | GFG | Majority Element - More Than n/3 |
| `LC_1832` | LC | Check if the Sentence Is Pangram |
| `LC_217` | LC | Contains Duplicate |
| `LC_219` | LC | Contains Duplicate II |
| `LC_242` | LC | Valid Anagram |
| `LC_2657` | LC | Find the Prefix Common Array of Two Arrays |
| `LC_229` | LC | Majority Element II |
| `LC_349` | LC | Intersection of Two Arrays |
| `LC_350` | LC | Intersection of Two Arrays II |
| `LC_3731` | LC | Find Missing Elements in Range |

### Heaps

| Folder | Source | Problem |
| --- | --- | --- |
| `Basics` | — | Min/Max Heap (core implementation) |
| `GFG_Check_If_An_Array_Is_Max_Heap` | GFG | Check if an Array Is a Max Heap |
| `GFG_Heap_Sort` | GFG | Heap Sort |
| `GFG_Height_Of_Heap` | GFG | Height of Heap |
| `GFG_KLargest` | GFG | K Largest Elements |
| `GFG_Min_Cost_to_Connect_Ropes` | GFG | Min Cost to Connect Ropes |
| `GFG_Nearly_Sorted` | GFG | Sort a Nearly Sorted (K-Sorted) Array |
| `LC_215` | LC | Kth Largest Element in an Array |
| `LC_347` | LC | Top K Frequent Elements |
| `LC_1046` | LC | Last Stone Weight |
| `LC_378` | LC | Kth Smallest Element in a Sorted Matrix |

### Math

| Folder | Source | Problem |
| --- | --- | --- |
| `LC_268` | LC | Missing Number |
| `LC_69` | LC | Sqrt(x) |
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

### Searching

| Folder | Source | Problem |
| --- | --- | --- |
| `GFG_Peak_in_Array` | GFG | Peak in Array |
| `GFG_Search_in_Rotated_Sorted_Array` | GFG | Search in Rotated Sorted Array |
| `GFG_Sorted_and_Rotated_Minimum` | GFG | Sorted and Rotated Minimum |
| `LC_33` | LC | Search in Rotated Sorted Array |
| `LC_81` | LC | Search in Rotated Sorted Array II |
| `LC_153` | LC | Find Minimum in Rotated Sorted Array |

### Singly Linked List

| Folder | Source | Problem |
| --- | --- | --- |
| `LC_92` | LC | Reverse Linked List II |

### Sorting

| Folder | Source | Problem |
| --- | --- | --- |
| `LC_1913` | LC | Maximum Product Difference Between Two Pairs |
| `LC_2037` | LC | Minimum Number of Moves to Seat Everyone |
| `GFG_Sort_0s_1s_2s` | GFG | Sort 0s 1s 2s |
| `LC_75` | LC | Sort Colors |
| `LC_910` | LC | Smallest Range II |

### Stack

| Folder | Source | Problem |
| --- | --- | --- |
| `Basics` | — | Stack (core implementation) |
| `GFG_Infix_Expression_Evaluation` | GFG | Infix Expression Evaluation |
| `GFG_Reverse_Stack` | GFG | Reverse a Stack |
| `GFG_Sort_Stack` | GFG | Sort a Stack |
| `LC_150` | LC | Evaluate Reverse Polish Notation |
| `LC_20` | LC | Valid Parentheses |
| `LC_224` | LC | Basic Calculator |
| `LC_225` | LC | Implement Stack using Queues |
| `LC_227` | LC | Basic Calculator II |
| `LC_496` | LC | Next Greater Element I |

## Stats

- **10** categories · **93** problems/data-structure implementations
- Each problem ships with a self-contained test.

---

*LC = LeetCode · GFG = GeeksforGeeks*
