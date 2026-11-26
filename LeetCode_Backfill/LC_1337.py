class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dic = [] 
        for  i in range(len(mat)):
            soldier_count = 0 
            for val in mat[i]:
                if val == 1:
                    soldier_count += 1
                else:
                    break

            dic.append((soldier_count,i))
        dic.sort()
        result = []
        for i in range(k):
            result.append(dic[i][1])
        return result
        