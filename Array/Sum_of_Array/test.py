from Array.Sum_of_Array.code import Solution


def run_test(arr, expected):
    sol = Solution()
    result = sol.arraySum(arr)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: arraySum({arr})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Sum of Array ===\n")
run_test([], 0)
run_test([1], 1)
run_test([1, 2, 3, 4, 5], 15)
run_test([10, 20, 30], 60)
run_test([-1, -2, -3], -6)
run_test([-1, 1, -2, 2], 0)
run_test([0, 0, 0], 0)
run_test([1, 1, 2, 2, 3, 3], 12)
run_test([1000000, 2000000, 3000000], 6000000)
run_test([5, 5, 5, 5], 20)