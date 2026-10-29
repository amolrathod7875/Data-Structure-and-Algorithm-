from Array.GFG_Rotate_Array_By_One.code import Solution


def run_test(arr, expected):
    sol = Solution()
    original = list(arr)
    sol.rotate(arr)
    result = arr

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: rotate({original})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Rotate Array by One ===\n")
run_test([1, 2, 3, 4, 5], [5, 1, 2, 3, 4])
run_test([1], [1])
run_test([], [])
run_test([1, 2], [2, 1])
run_test([0, 1, 2], [2, 0, 1])
run_test([1, 1, 1, 1], [1, 1, 1, 1])
run_test([-1, -2, -3, -4], [-4, -1, -2, -3])
run_test([5, 5, 6, 6, 7], [7, 5, 5, 6, 6])
run_test([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 1, 2, 3, 4, 5, 6, 7, 8, 9])
