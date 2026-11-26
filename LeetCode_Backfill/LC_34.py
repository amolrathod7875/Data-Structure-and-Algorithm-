from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(is_first: bool) -> int:
            left, right = 0, len(nums) - 1
            bound_index = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    # Target found, record the index
                    bound_index = mid
                    # If looking for the first occurrence, keep searching left
                    if is_first:
                        right = mid - 1
                    # If looking for the last occurrence, keep searching right
                    else:
                        left = mid + 1
                        
            return bound_index

        # Find the first occurrence (left extreme)
        left_extreme = find_bound(True)
        
        # Minor optimization: If the target isn't in the array at all, return early
        if left_extreme == -1:
            return [-1, -1]
        
        # Find the last occurrence (right extreme)
        right_extreme = find_bound(False)
        
        return [left_extreme, right_extreme]