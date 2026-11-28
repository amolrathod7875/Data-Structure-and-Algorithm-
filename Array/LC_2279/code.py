class Solution:
    def maximumBags(
        self, capacity: list[int], rocks: list[int], additionalRocks: int
    ) -> int:
        deficits = sorted(limit - current for limit, current in zip(capacity, rocks))
        filled = 0
        for deficit in deficits:
            if deficit > additionalRocks:
                break
            additionalRocks -= deficit
            filled += 1
        return filled
