from Sorting.LC_75.code import Solution


def run_test(nums, expected):
    sol = Solution()
    arr = list(nums)
    sol.sortColors(arr)
    result = arr

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: sortColors({nums})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 75: Sort Colors ===\n")
run_test([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2])
run_test([2, 0, 1], [0, 1, 2])
run_test([0], [0])
run_test([1], [1])
run_test([2], [2])
run_test([], [])
run_test([1, 2, 0], [0, 1, 2])
