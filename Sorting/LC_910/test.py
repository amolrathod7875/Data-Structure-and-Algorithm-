from Sorting.LC_910.code import Solution


def run_test(nums, k, expected):
    sol = Solution()
    result = sol.smallestRangeII(list(nums), k)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: smallestRangeII({nums}, {k})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 910: Smallest Range II ===\n")
run_test([1], 0, 0)
run_test([0, 10], 2, 6)
run_test([1, 3, 6], 3, 3)
run_test([7, 8, 8], 5, 1)
run_test([2, 7, 2], 1, 3)
