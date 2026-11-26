class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        seen = Counter(nums)
        Sum = 0
        for key, value in seen.items():
            if value == 1:
                Sum += key
        return Sum 