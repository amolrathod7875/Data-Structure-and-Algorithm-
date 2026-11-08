# LC 81 Search in Rotated Sorted Array II

## Problem

Search target in rotated sorted array with duplicates.

## Approach

Binary search with duplicate handling.

## Complexity

O(n) worst, O(log n) average; O(1) space.

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
python -m Searching.LC_81.test
```
