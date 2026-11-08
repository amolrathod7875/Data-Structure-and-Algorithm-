# LC 33 Search in Rotated Sorted Array

## Problem

Search target in rotated sorted array (distinct values).

## Approach

Binary search using sorted half.

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
python -m Searching.LC_33.test
```
