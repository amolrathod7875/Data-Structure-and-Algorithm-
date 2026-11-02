from Array.GFG_Minimize_the_Heights.code import Solution


def run_test(arr, k, expected):
    sol = Solution()
    result = sol.getMinDiff(list(arr), k)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: getMinDiff({arr}, {k})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Minimize the Heights ===\n")
run_test([1, 5, 8, 10], 2, 5)
run_test([3, 9, 12, 16, 20], 3, 11)
run_test([1, 10, 14, 14, 14, 15], 6, 5)
run_test([2, 6, 3, 4, 7, 2, 10, 3, 2, 1], 5, 7)
run_test([1], 5, 0)
