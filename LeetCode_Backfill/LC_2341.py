class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        pairs = 0
        left = 0

        for count in freq.values():
            pairs += count // 2
            left += count % 2
        return [pairs,left]