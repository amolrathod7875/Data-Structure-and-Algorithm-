class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        
        # Traverse the array from right to left
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits # No carry needed, we are done
            
            # If the digit is 9, it becomes 0. The loop continues to carry the 1.
            digits[i] = 0
            
        # If the loop finishes without returning, it means all digits were 9 (e.g., [9, 9, 9])
        # We need an extra digit at the front (e.g., [1, 0, 0, 0])
        return [1] + digits
        