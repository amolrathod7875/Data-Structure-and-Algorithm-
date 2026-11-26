class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        freq = {} 
        for num in nums:
            target1 = num - k
            target2 = num + k

            if target1 in freq:
                count += freq[target1]
            if target2 in freq:
                count += freq[target2]
            
            freq[num] = freq.get(num,0) + 1
        return count 