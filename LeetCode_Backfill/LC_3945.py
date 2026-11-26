class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        frequency = {}
        for ch in str(n):
            digits = int(ch)
            frequency[digits] = frequency.get(digits,0) + 1
        score = 0
        for digit, count in frequency.items():
            score += digit * count
        return score 