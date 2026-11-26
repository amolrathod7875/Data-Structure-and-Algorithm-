class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_avail = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in num_avail:
                return [i,num_avail[val]]
            else:
                num_avail[nums[i]] = i
        return []
        