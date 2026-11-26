class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        if n <= 1:
            return True
        max_reach = 0
        for i in range(n-1):
            if i > max_reach:
                return False
            
            max_reach = max(max_reach,i+nums[i])
            if max_reach >= n - 1:
                return True 
        return False
        