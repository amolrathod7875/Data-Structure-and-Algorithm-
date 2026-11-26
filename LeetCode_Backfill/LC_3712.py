class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        result = 0
        seen = Counter(nums)
        for value, count in seen.items():
            if count % k == 0:
                result += (value * count)
        return result