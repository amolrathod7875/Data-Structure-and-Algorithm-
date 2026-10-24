from Array.LC_1877.code import Solution


def run_test(nums, expected):
    sol = Solution()
    original = list(nums)
    result = sol.minPairSum(nums)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: minPairSum({original})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 1877: Minimize Maximum Pair Sum in Array ===\n")
run_test([3, 5, 2, 3], 7)
run_test([3, 5, 4, 2, 4, 6], 8)
run_test([1, 1, 1, 1], 2)
run_test([1, 2], 3)
run_test([1, 2, 3, 4], 5)
run_test([1, 2, 3, 4, 5, 6], 7)
run_test([5, 5, 5, 5, 5, 5], 10)
run_test([-1, -2, -3, -4], -5)
run_test([10, 20, 30, 40], 50)
run_test([1, 100, 2, 99], 101)
run_test([0, 0, 0, 0], 0)