# GFG Kadane's Algorithm

## Problem

Maximum subarray sum.

## Approach

Kadane: maxEnding = max(maxEnding + x, x); track global max.

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
python -m Array.GFG_Kadanes_Algorithm.test
```
