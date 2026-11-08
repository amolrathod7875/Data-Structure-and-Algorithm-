# GFG Sorted and Rotated Minimum

## Problem

Find minimum in sorted and rotated array.

## Approach

Binary search comparing mid with high.

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
python -m Searching.GFG_Sorted_and_Rotated_Minimum.test
```
