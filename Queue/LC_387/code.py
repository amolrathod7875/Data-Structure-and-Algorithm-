from collections import deque, Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        queue = deque()

        for i, char in enumerate(s):
            queue.append(i)
            while queue and freq[s[queue[0]]] > 1:
                queue.popleft()

        return queue[0] if queue else -1
