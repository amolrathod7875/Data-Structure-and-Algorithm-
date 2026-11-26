class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        seen = set()
        duplicate = False
        for num in nums:
            if num > n :
                return False
            if num in seen :
                if num < n or duplicate:
                    return False
                duplicate =True 
                continue
            seen.add(num)
        return True 
        