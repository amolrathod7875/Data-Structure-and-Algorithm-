class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            max_length = 0
            start = 0
            seen = {}
            for i in range(len(s)):
                char = s[i]
                if char in seen:
                    start = max(start,seen[char] + 1)
                max_length = max(max_length, i - start + 1)
                seen[char] = i

            return max_length
            


