class Solution:
    def findMajority(self, arr):
        n = len(arr)
        freq = {} 
        result = [] 
        
        for num in arr : 
            if num in freq :
                freq[num] += 1 
            else:
                freq[num] = 1 
        
        for num, count in freq.items():
            if count > n // 3 : 
                result.append(num)
        
        result.sort()
        return result
