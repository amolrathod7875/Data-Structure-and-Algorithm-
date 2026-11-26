class Solution(object):
    def leastInterval(self, tasks, n):
        from collections import Counter
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())
        max_freq_count = sum(1 for count in task_counts.values() if count == max_freq)
        intervals = (max_freq - 1) * (n + 1) + max_freq_count
        return max(intervals, len(tasks))
        