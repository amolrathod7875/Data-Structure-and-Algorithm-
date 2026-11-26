class Solution(object):
    def findClosest(self, x, y, z):
        x1 = abs(x - z)
        y1 = abs(y - z)

        if x1<y1:
            return 1
        elif x1>y1:
            return 2
        else:
            return 0