class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        suffix_count = Counter(nums)
        prefix_count = set()
        result = []
        for num in nums :
            prefix_count.add(num)
            suffix_count[num] -= 1
            if suffix_count[num] == 0:
                del suffix_count[num]
            diff = len(prefix_count) - len(suffix_count)
            result.append(diff)
        return result