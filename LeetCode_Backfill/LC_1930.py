class Solution(object):
    def countPalindromicSubsequence(self, s):
        res = 0
        for ci in range(ord('a'),ord('z')+1):
            c = chr(ci)
            left = s.find(c)
            right =s.rfind(c)
            if left != -1 and left < right:
                mid = set(s[left+1:right])
                res += len(mid)

        return res