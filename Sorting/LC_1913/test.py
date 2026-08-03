from Sorting.LC_1913.code import Solution


def run_test(nums, expected):
    sol = Solution()
    result = sol.maxProductDifference(nums)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: maxProductDifference({nums})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 1913: Maximum Product Difference Between Two Pairs ===\n")
run_test([5, 6, 2, 7, 4], 34)
run_test([4, 2, 5, 9, 7, 4, 8], 64)
run_test([1, 2, 3, 4], 10)
run_test([10, 20, 30, 40], 1000)
run_test([1, 1, 1, 1], 0)
run_test([100, 2, 1, 50], 4998)
run_test([5, 5, 5, 5], 0)
run_test([1, 1, 2, 2], 3)
run_test([1, 2, 3, 4, 5, 6], 28)
