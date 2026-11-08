# GFG Majority Element - More Than n/3

## Problem

Return all elements that appear more than n/3 times, sorted.

## Approach

Frequency map; collect keys with count > n//3, sort.

## Complexity

O(n) time, O(n) space.

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
python -m Hash_Map.GFG_Majority_Element_More_Than_n_3.test
```
