class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Quick optimization: If the note is longer, it's impossible
        if len(ransomNote) > len(magazine):
            return False
            
        magazine_counts = {}
        
        # 1. Build the inventory
        for char in magazine:
            magazine_counts[char] = magazine_counts.get(char, 0) + 1
            
        # 2. Consume the inventory
        for char in ransomNote:
            # If the character isn't in our map, or the count has reached 0
            if magazine_counts.get(char, 0) == 0:
                return False
            
            # Deduct the used letter
            magazine_counts[char] -= 1
            
        return True
        