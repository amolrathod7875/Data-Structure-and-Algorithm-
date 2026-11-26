class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = neg = zero = 0
        for num in nums :
            if num == 0:
                zero += 1
            elif num > 0:
                pos += 1
            else:
                neg += 1
        return max(pos,neg)