from Array.LC_3194.code import Solution


def run_test(nums, expected):
    sol = Solution()
    original = list(nums)
    result = sol.minimumAverage(nums)

    status = "PASS" if abs(result - expected) < 1e-9 else "FAIL"
    print(f"{status}: minimumAverage({original})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 3194: Minimum Average of Smallest and Largest Elements ===\n")
run_test([7, 8, 3, 4, 15, 13, 4, 1], 5.5)
run_test([1, 9, 8, 3, 10, 5], 5.5)
run_test([1, 2, 3, 4], 2.5)
run_test([1, 1, 1, 1], 1.0)
run_test([1, 100], 50.5)
run_test([5, 5, 5, 5, 5, 5], 5.0)
run_test([1, 2, 3, 4, 5, 6, 7, 8], 4.5)
run_test([10, 20, 30, 40, 50, 60], 35.0)
run_test([2, 7], 4.5)
run_test([100000, 1, 100000, 1], 50000.5)