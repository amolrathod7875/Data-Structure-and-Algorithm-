class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        seen = set(nums)

        for num in nums:
            reversedNum = int(str(num)[::-1])
            seen.add(reversedNum)
        return len(seen)