from Array.Smallest_Positive_Missing.code import Solution


def run_test(arr, expected):
    sol = Solution()
    result = sol.missingNumber(list(arr))

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: missingNumber({arr})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== Smallest Positive Missing ===\n")
run_test([1, 2, 3, 4, 5], 6)
run_test([0, -1, 3, 1], 2)
run_test([1, 1, 1], 2)
run_test([], 1)
run_test([2, 3, 4], 1)
run_test([1, 2, 0], 3)
