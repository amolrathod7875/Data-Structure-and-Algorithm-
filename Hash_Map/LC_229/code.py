class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums) 
        freq = {} 
        result = [] 
        for num in nums : 
            if num in freq : 
                freq[num] += 1 
            else:
                freq[num] = 1 
        for num, count in freq.items() :
            if count > n // 3  :
                result.append(num)
            
        result.sort()
        return result
