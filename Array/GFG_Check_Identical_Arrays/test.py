from Array.GFG_Check_Identical_Arrays.code import Solution


def run_test(a, b, expected):
    sol = Solution()
    result = sol.checkIdentical(a, b)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: checkIdentical({a}, {b})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Check Identical Arrays ===\n")
run_test([1, 2, 3], [1, 2, 3], True)
run_test([1, 2, 3], [1, 2, 4], False)
run_test([1, 2, 3], [1, 2], False)
run_test([], [], True)
run_test([1], [1], True)
run_test([1], [2], False)
run_test([5, 5, 5], [5, 5, 5], True)
run_test([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], True)
run_test([1, 2, 3], [3, 2, 1], False)
run_test([-1, -2, -3], [-1, -2, -3], True)
run_test([0, 0, 0], [0, 0, 0], True)
run_test([10, 20, 30], [10, 20, 31], False)