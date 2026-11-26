class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)

        max_freq = -1 
        for num, count in freq.items():
            if num == count :
                if num > max_freq:
                    max_freq = num

        return max_freq

        