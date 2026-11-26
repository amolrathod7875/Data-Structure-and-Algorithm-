class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 0
        target = (len(nums)) / 2
        for key, value in freq.items():
            if value >= target:
                ans = max(ans,key) 
        return ans     