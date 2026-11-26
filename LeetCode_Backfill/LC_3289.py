class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        empty_set = set()
        res = []
        for id in nums:
            if id in empty_set:
                res.append(id)
            else:
                empty_set.add(id)
        return res
        