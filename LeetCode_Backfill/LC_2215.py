class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ansArr1 = []
        ansArr2 = []
        arr1 = set(nums1)
        arr2 = set(nums2)
        
        for i in nums1:
            if i not in arr2:
                ansArr1.append(i)
        for j in nums2:
            if j not in arr1:
                ansArr2.append(j)
        return [list(set(ansArr1)),list(set(ansArr2))]