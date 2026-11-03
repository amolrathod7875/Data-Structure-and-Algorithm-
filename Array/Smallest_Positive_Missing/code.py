class Solution:
    def missingNumber(self, arr):
        audit = set(arr)
        missing = 1 
        while missing in audit :
            missing += 1 
        return missing
