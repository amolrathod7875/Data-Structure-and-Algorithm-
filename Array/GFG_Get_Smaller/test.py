from Array.GFG_Get_Smaller.code import Solution


def run_test(arr, target, expected):
    sol = Solution()
    result = sol.getSmaller(arr, target)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: getSmaller({arr}, {target})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Get Smaller in Array ===\n")
run_test([1, 2, 3, 4, 5], 4, [1, 2, 3])
run_test([1, 2, 3, 4, 5], 1, [])
run_test([1, 2, 3, 4, 5], 6, [1, 2, 3, 4, 5])
run_test([], 5, [])
run_test([10, 20, 30], 25, [10, 20])
run_test([5, 5, 5], 5, [])
run_test([-1, -2, -3, 0, 1], 0, [-1, -2, -3])
run_test([7], 7, [])
run_test([7], 8, [7])
run_test([2, 4, 6, 8, 10], 5, [2, 4])