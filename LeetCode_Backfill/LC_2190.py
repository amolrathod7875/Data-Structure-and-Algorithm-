class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        freq = {}
        for i in range(len(nums) -1):
            if nums[i] == key:
                target = nums[i+1]
                freq[target] = freq.get(target,0) + 1
        mx = 0
        ans = -1 

        for num,count in freq.items():
            if count > mx:
                mx = count 
                ans = num
        return ans