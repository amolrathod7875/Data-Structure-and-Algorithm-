from Array.GFG_Alternates_in_Array.code import Solution


def run_test(arr, expected):
    sol = Solution()
    result = sol.getAlternates(arr)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: getAlternates({arr})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Alternates in Array ===\n")
run_test([], [])
run_test([1], [1])
run_test([1, 2], [1])
run_test([1, 2, 3, 4, 5], [1, 3, 5])
run_test([10, 20, 30, 40], [10, 30])
run_test([-1, -2, -3, -4], [-1, -3])
run_test([0, 0, 0, 0], [0, 0])
run_test([1, 1, 2, 2, 3, 3], [1, 2, 3])
