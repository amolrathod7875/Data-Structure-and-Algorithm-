# GFG Count Occurrences in Sorted

## Problem

Count occurrences of target in sorted array.

## Approach

Linear scan counting matches.

## Complexity

O(n) time, O(1) space.

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
python -m Array.GFG_Count_Occurrences_in_Sorted.test
```
