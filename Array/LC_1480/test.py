from Array.LC_1480.code import Solution


def run_test(nums, expected):
    sol = Solution()
    result = sol.runningSum(nums)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: runningSum({nums})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 1480: Running Sum of 1d Array ===\n")
run_test([], [])
run_test([1], [1])
run_test([1, 2, 3, 4], [1, 3, 6, 10])
run_test([1, 1, 1, 1, 1], [1, 2, 3, 4, 5])
run_test([3, 1, 2, 10, 1], [3, 4, 6, 16, 17])
run_test([-1, -2, -3], [-1, -3, -6])
run_test([0, 0, 0], [0, 0, 0])
