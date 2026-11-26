class Solution(object):
    def heightChecker(self, heights):
        n = len(heights)
        count = 0
        sort_ht = sorted(heights)
        for i in range(n):
            if heights[i] != sort_ht[i]:
                count += 1

        return count


        