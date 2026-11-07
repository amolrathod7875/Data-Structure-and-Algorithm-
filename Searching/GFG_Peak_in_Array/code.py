class Solution:   
    def peakElement(self, arr):
        left = 0 
        right = len(arr) - 1 
        while left < right :
            mid = (left + right ) // 2 
            if arr[mid] > arr[mid + 1 ]:
                right = mid
            else:
                left = mid + 1 
        return left
