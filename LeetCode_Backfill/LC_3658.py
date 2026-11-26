class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        import math
        sumOdd = n*n
        sumEven = n * (n+1)
        return math.gcd(sumOdd,sumEven)