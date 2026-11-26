class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            if num % 2 == 0:
                result.append(0)
            else:
                result.append(1)

        low = mid = 0
        high = len(result) - 1

        while mid <= high:
            if result[mid] == 0:
                result[low], result[mid] = result[mid], result[low]
                low += 1
                mid += 1
            else:  # result[mid] == 1
                mid += 1

        return result