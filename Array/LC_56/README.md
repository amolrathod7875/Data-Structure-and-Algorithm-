# LC 56 Merge Intervals

## Problem

Merge all overlapping intervals.

## Approach

Sort by start; merge if current start <= prev end.

## Complexity

O(n log n) time, O(n) space.

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
python -m Array.LC_56.test
```
