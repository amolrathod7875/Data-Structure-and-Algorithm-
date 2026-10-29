from Array.Reverse_Array.code import Solution


def run_test(arr, expected):
    sol = Solution()
    original = list(arr)
    result = sol.reverseArray(arr)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: reverseArray({original})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Reverse Array ===\n")
run_test([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
run_test([1, 2, 3, 4], [4, 3, 2, 1])
run_test([1], [1])
run_test([], [])
run_test([1, 2], [2, 1])
run_test([0, 0, 0], [0, 0, 0])
run_test([-1, -2, -3], [-3, -2, -1])
run_test([1, 1, 2, 2, 3, 3], [3, 3, 2, 2, 1, 1])
run_test([10, 20, 30, 40, 50, 60, 70], [70, 60, 50, 40, 30, 20, 10])
run_test([5, 5, 5, 5], [5, 5, 5, 5])