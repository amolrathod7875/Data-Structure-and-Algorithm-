class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSizes.sort()
        bobSizes.sort()
        i = j = 0
        target = (sum(bobSizes) - sum(aliceSizes)) // 2
        while i < len(aliceSizes) and j < len(bobSizes) :
            curr = bobSizes[j] - aliceSizes[i]

            if curr == target:
                return [aliceSizes[i],bobSizes[j]]
            elif curr < target:
                j += 1
            else:
                i += 1
        return []