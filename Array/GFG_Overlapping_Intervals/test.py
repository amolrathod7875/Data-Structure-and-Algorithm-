from Array.GFG_Overlapping_Intervals.code import Solution


def run_test(arr, expected):
    sol = Solution()
    result = sol.mergeOverlap([list(x) for x in arr])

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: mergeOverlap({arr})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Overlapping Intervals ===\n")
run_test([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]])
run_test([[1,4],[4,5]], [[1,5]])
run_test([], [])
run_test([[1,2]], [[1,2]])
run_test([[1,5],[2,3],[4,6]], [[1,6]])
