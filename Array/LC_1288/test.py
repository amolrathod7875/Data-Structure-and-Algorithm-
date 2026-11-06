from Array.LC_1288.code import Solution


def run_test(intervals, expected):
    sol = Solution()
    result = sol.removeCoveredIntervals([list(x) for x in intervals])

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: removeCoveredIntervals({intervals})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 1288: Remove Covered Intervals ===\n")
run_test([[1,4],[3,6],[2,8]], 2)
run_test([[1,4],[2,3]], 1)
run_test([[1,2],[1,4],[3,4]], 1)
run_test([], 0)
run_test([[1,2]], 1)
