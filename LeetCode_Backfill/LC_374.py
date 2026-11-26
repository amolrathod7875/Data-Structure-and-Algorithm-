# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        
        while left <= right:
            # Use this formula to prevent potential integer overflow
            # (though Python handles arbitrarily large integers, it's a good habit)
            mid = left + (right - left) // 2 
            
            result = guess(mid)
            
            if result == 0:
                # We found the number
                return mid
            elif result == 1:
                # The picked number is higher, so search the right half
                left = mid + 1
            else:
                # The picked number is lower, so search the left half
                right = mid - 1
                
        return -1
        