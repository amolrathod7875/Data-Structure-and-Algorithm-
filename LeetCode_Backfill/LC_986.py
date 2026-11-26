class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i = j = 0
        n, m = len(firstList),len(secondList)
        
        while i < n and j < m :
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]

            low = max(start1,start2)
            high = min(end1,end2)

            if low <= high  :
                result.append([low, high])

            if end1 > end2:
                j += 1
            else:
                i += 1

        return result
