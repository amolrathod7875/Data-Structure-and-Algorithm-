# LC 153 Find Minimum in Rotated Sorted Array

## Problem

Find minimum in rotated sorted array (distinct values).

## Approach

Binary search comparing mid with right.

## Complexity

O(log n) time, O(1) space.

```mermaid
flowchart TD
    A["Input"] --> B["Initialize"]
    B --> D["Process elements"]
    D --> E{"More elements?"}
    E -->|Yes| F["Process current"]
    F --> E
    E -->|No| G["Return result"]
```

## Run Tests

```bash
python -m Searching.LC_153.test
```
