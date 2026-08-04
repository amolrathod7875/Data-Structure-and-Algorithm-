class Solution:
    def findPrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        freq = {}
        common = 0
        ans = []

        for i in range(len(A)):
            freq[A[i]] = freq.get(A[i], 0) + 1
            if freq[A[i]] == 2:
                common += 1

            freq[B[i]] = freq.get(B[i], 0) + 1
            if freq[B[i]] == 2:
                common += 1

            ans.append(common)

        return ans
