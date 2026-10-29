from Array.GFG_Smallest_in_Array.code import Solution


def run_test(arr, expected):
    sol = Solution()
    result = sol.findMin(arr)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: findMin({arr})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Smallest in Array ===\n")
run_test([1, 2, 3, 4, 5], 1)
run_test([5, 4, 3, 2, 1], 1)
run_test([3, 1, 4, 1, 5], 1)
run_test([42], 42)
run_test([-1, -3, -2, -5, 0], -5)
run_test([0, 0, 0, 0], 0)
run_test([10, 20, 30], 10)
run_test([7, 7, 7, 7], 7)
run_test([-5, -10, -3, -1], -10)
run_test([100, 50, 25, 75], 25)
run_test([1, 1, 1, 2, 2, 2], 1)