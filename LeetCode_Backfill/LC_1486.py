class Solution(object):
    def xorOperation(self, n, start):
        res = 0
        for i in range(n):
            num = start + 2 * i
            res ^= num
        return res
        