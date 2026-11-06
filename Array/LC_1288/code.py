class Solution:
    def removeCoveredIntervals(self, interval: list[list[int]]) -> int:
        count = 0 
        max_end = 0 
        interval.sort(key=lambda x:(x[0], -x[1]))
        for start, end in interval:
            if end > max_end:
                count += 1 
                max_end = end
        return count
