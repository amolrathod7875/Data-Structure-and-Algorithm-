from Array.GFG_Move_All_Zeroes_to_End.code import Solution


def run_test(arr, expected):
    sol = Solution()
    original = list(arr)
    result = sol.pushZerosToEnd(arr)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: pushZerosToEnd({original})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Move All Zeroes to End ===\n")
run_test([1, 2, 0, 4, 3, 0, 5, 0], [1, 2, 4, 3, 5, 0, 0, 0])
run_test([10, 20, 30], [10, 20, 30])
run_test([0, 0], [0, 0])
run_test([0], [0])
run_test([1], [1])
run_test([], [])
run_test([0, 1, 0, 3, 12], [1, 3, 12, 0, 0])
run_test([1, 0, 2, 0, 3, 0], [1, 2, 3, 0, 0, 0])
run_test([0, 0, 0, 1, 2, 3], [1, 2, 3, 0, 0, 0])
run_test([4, 2, 4, 0, 0, 3, 0, 5, 1, 0], [4, 2, 4, 3, 5, 1, 0, 0, 0, 0])
run_test([0, 0, 1, 0, 0, 0, 2, 0, 3], [1, 2, 3, 0, 0, 0, 0, 0, 0])