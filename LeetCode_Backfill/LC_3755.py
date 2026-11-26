class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        n = nums
        m = {(0, 0): 0}
        l, x, b = 0, 0, 0
        N = len(n)
        
        for k in range(1, N + 1):
            num = n[k - 1]
            x ^= num
            b += 1 if num % 2 else -1
                
            s = (x, b)
            
            if s in m:
                l = max(l, k - m[s])
            else:
                m[s] = k
                
        return l