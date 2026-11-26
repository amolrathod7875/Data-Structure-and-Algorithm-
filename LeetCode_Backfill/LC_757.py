class Solution(object):
    def intersectionSizeTwo(self, intervals):
        
        if not intervals:
            return 0

        # Sort by right endpoint ascending, and left endpoint descending
        intervals.sort(key=lambda x: (x[1], -x[0]))

        # s1 < s2 are the two largest selected integers so far
        s1 = -10**18
        s2 = -10**18
        ans = 0

        for a, b in intervals:
            if s1 >= a:
                # both s1 and s2 are inside [a, b]
                continue
            if s2 >= a:
                # only s2 is inside [a, b], add one more point (b)
                ans += 1
                s1 = s2
                s2 = b
            else:
                # neither s1 nor s2 is inside [a, b], add two points (b-1, b)
                ans += 2
                s1 = b - 1
                s2 = b

        return ans