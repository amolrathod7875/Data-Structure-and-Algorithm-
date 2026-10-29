from Array.GFG_End_Insert.code import Solution


def run_test(arr, val, expected):
    sol = Solution()
    original = list(arr)
    result = sol.insertAtEnd(arr, val)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: insertAtEnd({original}, {val})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Insert at End of Array ===\n")
run_test([], 1, [1])
run_test([1], 2, [1, 2])
run_test([1, 2, 3], 4, [1, 2, 3, 4])
run_test([5], 5, [5, 5])
run_test([0, 0, 0], 0, [0, 0, 0, 0])
run_test([1, 2, 3, 4, 5], 6, [1, 2, 3, 4, 5, 6])
run_test([-1, -2], -3, [-1, -2, -3])
run_test([10], 20, [10, 20])
run_test([1, 1, 2, 2], 3, [1, 1, 2, 2, 3])