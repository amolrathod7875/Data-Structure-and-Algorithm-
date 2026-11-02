from Array.GFG_Kadanes_Algorithm.code import Solution


def run_test(arr, expected):
    sol = Solution()
    result = sol.maxSubarraySum(arr)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: maxSubarraySum({arr})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Kadane's Algorithm ===\n")
run_test([1, 2, 3, -2, 5], 9)
run_test([-1, -2, -3, -4], -1)
run_test([5], 5)
run_test([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
run_test([1, -2, 3, 4, -1], 7)
