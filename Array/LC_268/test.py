from Array.LC_268.code import Solution


def run_test(nums, expected):
    sol = Solution()
    original = list(nums)
    result = sol.missingNumber(nums)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: missingNumber({original})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 268: Missing Number ===\n")
run_test([3, 0, 1], 2)
run_test([0, 1], 2)
run_test([9, 6, 4, 2, 3, 5, 7, 0, 1], 8)
run_test([0], 1)
run_test([1], 0)
run_test([0, 2], 1)
run_test([1, 2], 0)
run_test([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 21)
run_test([4, 0, 3, 1], 2)
run_test([8, 3, 5, 2, 4, 6, 0, 1], 7)