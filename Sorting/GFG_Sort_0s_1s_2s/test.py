from Sorting.GFG_Sort_0s_1s_2s.code import Solution


def run_test(arr, expected):
    sol = Solution()
    result = sol.sort012(list(arr))

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: sort012({arr})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Sort 0s, 1s and 2s ===\n")
run_test([0, 1, 2, 0, 1, 2], [0, 0, 1, 1, 2, 2])
run_test([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2])
run_test([2, 0, 1], [0, 1, 2])
run_test([], [])
run_test([1, 1, 1], [1, 1, 1])
run_test([2, 2, 2], [2, 2, 2])
run_test([0, 0, 0], [0, 0, 0])
