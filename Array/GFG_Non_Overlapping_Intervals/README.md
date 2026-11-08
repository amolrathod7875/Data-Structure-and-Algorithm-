# GFG Non-Overlapping Intervals

## Problem

Minimum number of intervals to remove so remaining are non-overlapping.

## Approach

Sort by end; greedily keep intervals with earliest end.

## Complexity

O(n log n) time, O(1) extra space.

```mermaid
flowchart TD
    A["Input"] --> B["Initialize"]
    B --> C["Sort array"]
    C --> D["Process elements"]
    D --> E{"More elements?"}
    E -->|Yes| F["Process current"]
    F --> E
    E -->|No| G["Return result"]
```

## Run Tests

```bash
python -m Array.GFG_Non_Overlapping_Intervals.test
```
