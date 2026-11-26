class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        max_len = 1
        
        # 2. Handle the special case for '1'
        if 1 in counts:
            ones = counts[1]
            if ones % 2 == 0:
                ones -= 1
            max_len = max(max_len, ones)
            
        # 3. Iterate through the unique numbers in our dictionary
        for num in counts:
            if num == 1:
                continue
            
            curr = num
            curr_len = 0
            
            # Use .get(curr, 0) to avoid KeyErrors if the square doesn't exist
            while counts.get(curr, 0) >= 2 and counts.get(curr**2, 0) >= 1:
                curr_len += 2       # Add one to the left, one to the right
                curr = curr**2      # Move up to the next square
            
            # Add the peak element
            curr_len += 1
            
            # Update the global maximum
            max_len = max(max_len, curr_len)
            
        return max_len
