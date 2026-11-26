class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = [0] * 1001 
        result = []
        for arr in nums:
            for num in arr:
                counts[num] += 1
        n = len(nums)
        for i in range(1,1001):
            if counts[i] == n:
                result.append(i)
        return result

        