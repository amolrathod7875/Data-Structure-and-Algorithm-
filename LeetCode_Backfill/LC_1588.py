class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        total_sum = 0
        for i in range(n):
            # Number of subarrays starting at or before index i.
            starts_before = i + 1
            # Number of subarrays ending at or after index i.
            ends_after = n - i

            # The total number of subarrays that include arr[i] is starts_before * ends_after.
            # We need to find how many of these have an odd length.
            # The number of odd-length subarrays is ceil(total_subarrays / 2).
            num_odd_subarrays = (starts_before * ends_after + 1) // 2
            
            total_sum += arr[i] * num_odd_subarrays
            
        return total_sum
        