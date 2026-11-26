class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        result = []
        for ch,count in sorted(freq.items(), key = lambda x: x[1], reverse=True):
            result.append(ch * count)
        return ''.join(result)