from Array.GFG_Array_Of_Pairs.code import Solution


def run_test(arr, expected):
    sol = Solution()
    result = sol.arrayOfPairs(arr)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: arrayOfPairs({arr})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Array of Pairs ===\n")
run_test([1, 2, 3, 4, 5], [[1, 5], [2, 4], [3, 3]])
run_test([1, 2, 3, 4], [[1, 4], [2, 3]])
run_test([1], [[1, 1]])
run_test([], [])
run_test([1, 2], [[1, 2]])
run_test([10, 20, 30, 40, 50, 60], [[10, 60], [20, 50], [30, 40]])
run_test([0, 0, 0, 0], [[0, 0], [0, 0]])
run_test([-1, -2, -3, -4], [[-1, -4], [-2, -3]])
run_test([5, 5, 5, 5, 5], [[5, 5], [5, 5], [5, 5]])
run_test([1, 2, 3, 4, 5, 6, 7], [[1, 7], [2, 6], [3, 5], [4, 4]])