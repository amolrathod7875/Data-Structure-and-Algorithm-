from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(capacity : int ) -> bool:
            days_needed = 1
            current_weight = 0
            for weight in weights:
                if current_weight + weight > capacity:
                    days_needed += 1
                    current_weight = 0
                current_weight += weight
            return days_needed <= days

        low, high = max(weights),sum(weights)
        while low < high :
            mid = low + (high - low ) // 2

            if helper(mid):
                high = mid
            else:
                low = mid + 1 

        return low
