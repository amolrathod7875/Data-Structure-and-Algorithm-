from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = n 
        result = []
        while i < n :
            result.append(nums[i])
            i += 1
            result.append(nums[j])
            j += 1 
        return result
