from Array.GFG_Next_Permutation.code import Solution


def run_test(arr, expected):
    sol = Solution()
    result = sol.nextPermutation(list(arr))

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: nextPermutation({arr})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Next Permutation ===\n")
run_test([1, 2, 3], [1, 3, 2])
run_test([3, 2, 1], [1, 2, 3])
run_test([1, 1, 5], [1, 5, 1])
run_test([1, 3, 2], [2, 1, 3])
run_test([2, 3, 1], [3, 1, 2])
run_test([1, 2, 3, 4], [1, 2, 4, 3])
run_test([4, 3, 2, 1], [1, 2, 3, 4])
run_test([1], [1])
run_test([], [])
