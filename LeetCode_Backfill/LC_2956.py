class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ansArr1, ansArr2 = 0,0
        for i in nums1:
            if i in nums2:
                ansArr1 += 1
        for j in nums2:
            if j in nums1:
                ansArr2 += 1
        return [ansArr1,ansArr2]