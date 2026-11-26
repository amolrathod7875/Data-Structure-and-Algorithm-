class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        diff = 0
        points.sort()
        for i in range(1,len(points)):
            diff = max(diff, points[i][0] - points[i-1][0])
        return diff 
        