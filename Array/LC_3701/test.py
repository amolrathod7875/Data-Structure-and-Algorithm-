from Array.LC_3701.code import Solution


def run_test(nums, expected):
    sol = Solution()
    result = sol.alternatingSum(nums)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: alternatingSum({nums})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 3701: Compute Alternating Sum ===\n")
run_test([1, 3, 5, 7], -4)
run_test([100], 100)
run_test([1, 2, 3, 4], -2)
run_test([5], 5)
run_test([1, 2], -1)
run_test([10, 20, 30], 20)
run_test([1, 1, 1, 1, 1], 1)
run_test([2, 4, 6, 8, 10], 6)
