from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        suffixes = list(range(n))
        ranks = nums[:]
        width = 1
        while width < n:
            suffixes.sort(key=lambda start: (
                ranks[start], ranks[start + width] if start + width < n else -1
            ))
            next_ranks = [0] * n
            for index in range(1, n):
                previous, current = suffixes[index - 1], suffixes[index]
                previous_key = (ranks[previous],
                                ranks[previous + width] if previous + width < n else -1)
                current_key = (ranks[current],
                               ranks[current + width] if current + width < n else -1)
                next_ranks[current] = next_ranks[previous] + (previous_key != current_key)
            ranks = next_ranks
            if ranks[suffixes[-1]] == n - 1:
                break
            width *= 2

        positions = [0] * n
        for index, start in enumerate(suffixes):
            positions[start] = index

        # lcp[index] compares suffixes[index] with its preceding suffix.
        lcp = [0] * n
        common = 0
        for start in range(n):
            index = positions[start]
            if index == 0:
                common = 0
                continue
            previous = suffixes[index - 1]
            while (start + common < n and previous + common < n
                   and nums[start + common] == nums[previous + common]):
                common += 1
            lcp[index] = common
            common = max(0, common - 1)

        answer = n
        for index, start in enumerate(suffixes):
            repeated = max(lcp[index], lcp[index + 1] if index + 1 < n else 0)
            candidate = repeated + 1
            if candidate <= n - start:
                answer = min(answer, candidate)
        return answer
