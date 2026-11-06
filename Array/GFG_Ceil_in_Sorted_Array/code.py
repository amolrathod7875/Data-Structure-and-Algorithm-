class Solution:
    def findCeil(self, arr, x):
        low = 0 
        high = len(arr) - 1 
        ans = -1 
        while low <= high :
            mid = (low + high) // 2 
            if arr[mid] >= x :
                ans = mid
                high = mid - 1 
            else:
                low = mid + 1
        return ans  

    def findCeilNaive(self, arr, x):
        for i, value in enumerate(arr):
            if value >= x:
                return i
        return -1
