class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        peak = 0
        curr_height = 0
        for alt in  gain:
            curr_height += alt
            peak = max(curr_height,peak)
        return peak
        