class Solution:
    def findGCD(self, nums: List[int]) -> int:
        import math 
        smallest = min(nums)
        largest = max(nums)
        return math.gcd(smallest,largest)