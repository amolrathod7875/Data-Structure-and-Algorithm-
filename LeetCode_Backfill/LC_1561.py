class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        starter = n // 3 
        result = 0
        while starter < n :
            result += piles[starter]
            starter += 2
        return result