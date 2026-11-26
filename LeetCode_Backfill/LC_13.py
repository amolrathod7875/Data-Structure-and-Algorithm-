class Solution:
    def romanToInt(self, s: str) -> int:
        # 1. Map each Roman numeral to its integer value
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        
        # 2. Iterate through the string
        for i in range(len(s)):
            # If the current numeral is less than the NEXT numeral, subtract it
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            # Otherwise, just add it to the total
            else:
                total += roman_map[s[i]]
                
        return total
        