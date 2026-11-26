class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = {}
        for num in nums :
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        return sorted(nums,key = lambda x : (frequency[x],-x))
        