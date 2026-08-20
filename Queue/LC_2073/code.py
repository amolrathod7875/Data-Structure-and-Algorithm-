from collections import deque


class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        queue = deque([(tickets[i], i) for i in range(len(tickets))])
        time = 0

        while queue:
            tickets_needed, idx = queue.popleft()
            tickets_needed -= 1
            time += 1

            if tickets_needed > 0:
                queue.append((tickets_needed, idx))
            elif idx == k:
                return time
