class Solution:
    def mergeArrays(self, a, b):
        audit = a + b 
        audit.sort()
        n = len(a)
        m = len(b)
        
        for i in range(n):
            a[i] = audit[i]
        
        for j in range(m):
            b[j] = audit[n + j]
