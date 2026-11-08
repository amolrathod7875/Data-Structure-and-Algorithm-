# LC 75 Sort Colors

## Problem

Sort array of 0s, 1s, 2s in-place (Dutch National Flag).

## Approach

Three pointers low, mid, high.

## Complexity

O(n) time, O(1) space.

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
python -m Sorting.LC_75.test
```
