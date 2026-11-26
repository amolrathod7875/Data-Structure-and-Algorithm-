class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        available = Counter(digits)
        ans = []

        for num in range(100, 1000, 2):
            needed = Counter(map(int, str(num)))

            valid = True
            for d, cnt in needed.items():
                if available[d] < cnt:
                    valid = False
                    break

            if valid:
                ans.append(num)

        return ans