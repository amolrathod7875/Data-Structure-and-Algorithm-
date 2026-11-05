# GFG Overlapping Intervals

## Problem

Merge all overlapping intervals.

## Approach

Sort by start; merge if current start <= prev end.

## Complexity

O(n log n) time, O(n) space.

## Run Tests

```bash
python -m Array.GFG_Overlapping_Intervals.test
```
