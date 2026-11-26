class Solution(object):
    def climbStairs(self, n):
        if (n==1):
            return 1 #if there is one single step then we can climb by one single way 

        a = 1
        b = 2 
        for i in range(3,n+1):
            curr_step = a + b 
            #current step = a(1) + b(2)
            a = b
            #simple swapping
            b = curr_step

        return b
        