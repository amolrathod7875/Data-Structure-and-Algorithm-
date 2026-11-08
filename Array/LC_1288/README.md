# LC 1288 Remove Covered Intervals

## Problem

Given intervals, remove those covered by another interval; return count of remaining.

## Approach

Sort by start asc, end desc; count intervals with end greater than max_end.

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
python -m Array.LC_1288.test
```
