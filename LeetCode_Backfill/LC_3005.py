class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        max_freq = 0
        for count in freq.values():
            if count > max_freq:
                max_freq = count
        total_max_freq_element = 0
        for count in freq.values():
            if count == max_freq:
                total_max_freq_element += count
        return total_max_freq_element