class Solution:
    def numberOfMatches(self, n: int) -> int:
        t=0
        while n > 1:
            if n % 2 == 0:
                n //= 2
                t += n
            else:
                n //= 2
                t += n+1
        return t