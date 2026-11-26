class Solution(object):
    def findMinArrowShots(self, points):
        if not points :
            return 0
        arrow_count = 1
        n = len(points)
        points.sort(key=lambda x : x[1])
        last_arrow_end = points[0][1]
        for i in range(1,n):
            current_state = points[i][0]
            if current_state > last_arrow_end:
                arrow_count += 1
                last_arrow_end = points[i][1]
        return arrow_count 
        