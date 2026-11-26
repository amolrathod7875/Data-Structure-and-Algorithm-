# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
        # Notice we use < instead of <= here
        while left < right:
            # (left + right) // 2 can cause integer overflow in languages like Java/C++, 
            # though Python handles arbitrarily large integers automatically. 
            # It's a good habit to write it this way:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                # The first bad version is at 'mid' or somewhere before it
                right = mid
            else:
                # The first bad version is strictly after 'mid'
                left = mid + 1
                
        # When left == right, we have found the boundary
        return left
        
        