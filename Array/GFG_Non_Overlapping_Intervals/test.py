from Array.GFG_Non_Overlapping_Intervals.code import Solution


def run_test(intervals, expected):
    sol = Solution()
    result = sol.minRemoval([list(x) for x in intervals])

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: minRemoval({intervals})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Non-Overlapping Intervals ===\n")
run_test([[1,2],[2,3],[3,4],[1,3]], 1)
run_test([[1,3],[1,3],[1,3]], 2)
run_test([[1,2],[1,2],[1,2]], 2)
run_test([[1,2],[2,3]], 0)
run_test([[0,2],[1,3],[2,4],[3,5],[4,6]], 2)
