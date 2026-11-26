class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)
        smallest_count = {}
        for i,num in enumerate (sorted_num):
            if num not in smallest_count:
                smallest_count[num] = i
        return [smallest_count[num] for num in nums]