from Array.Second_Largest.code import Solution


def run_test(arr, expected):
    sol = Solution()
    result = sol.getSecondLargest(arr)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: getSecondLargest({arr})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Second Largest ===\n")
run_test([1, 2, 3, 4, 5], 4)
run_test([5, 4, 3, 2, 1], 4)
run_test([1, 1, 1, 1], -1)
run_test([1, 2], 1)
run_test([2, 1], 1)
run_test([10, 10, 10, 5], 5)
run_test([5, 5, 4, 4, 3], 4)
run_test([-1, -2, -3, -4], -2)
run_test([0, 0, 0, 1], 0)
run_test([100], -1)
run_test([], -1)
run_test([3, 3, 3, 2, 2], 2)
run_test([7, 7, 7, 7, 6], 6)