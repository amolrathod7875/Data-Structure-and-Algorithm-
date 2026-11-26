class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        sorted_string = [''.join(sorted(i)) for i in strs]
        hash = {}
        for i in range(len(strs)):
            if sorted_string[i] in hash:
                hash[sorted_string[i]].append(strs[i])
            else:
                hash[sorted_string[i]] = [strs[i]]

        return list(hash.values())