class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float('inf')
        nums.sort() #O(N*LogN)
        n = len(nums)
        for i in range(n-2): #O(N)
            left, right = i + 1, n - 1 
            while left < right : #O(N^2)
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target ) < abs(closest - target):
                    closest = total
                
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1 
                else:
                    return target

        return closest




        