class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda x : x[1])
        n = len(intervals)
        kept_count = 1
        last_end = intervals[0][1]
        for i in range(1,n):
            current_start = intervals[i][0]
            if current_start >= last_end:
                kept_count += 1 
                last_end = intervals[i][1]

        min_removals = n - kept_count
        return min_removals