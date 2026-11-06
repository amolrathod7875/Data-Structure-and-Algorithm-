from Array.GFG_Insert_Interval.code import Solution


def run_test(intervals, newInterval, expected):
    sol = Solution()
    result = sol.insertInterval([list(x) for x in intervals], list(newInterval))

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: insertInterval({intervals}, {newInterval})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Insert Interval ===\n")
run_test([[1,3],[6,9]], [2,5], [[1,5],[6,9]])
run_test([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], [[1,2],[3,10],[12,16]])
run_test([], [5,7], [[5,7]])
run_test([[1,5]], [2,3], [[1,5]])
run_test([[1,5]], [6,8], [[1,5],[6,8]])
