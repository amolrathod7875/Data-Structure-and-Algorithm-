from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while (left <= right):
            middle = (left + right) // 2
            if nums[middle] == target:
                return True

            if nums[left] == nums[middle] and nums[middle] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[middle]:
                if target >= nums[left] and target < nums[middle]:
                    right = middle - 1
                else:   
                    left = middle + 1
            else:
                if target <= nums[right] and target > nums[middle]:
                    left = middle + 1 
                else:
                    right = middle - 1 
        return False
