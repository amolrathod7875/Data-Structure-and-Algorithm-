from Array.LC_56.code import Solution


def run_test(intervals, expected):
    sol = Solution()
    result = sol.merge([list(x) for x in intervals])

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: merge({intervals})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 56: Merge Intervals ===\n")
run_test([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]])
run_test([[1,4],[4,5]], [[1,5]])
run_test([], [])
run_test([[1,4],[0,4]], [[0,4]])
run_test([[1,4],[2,3]], [[1,4]])
