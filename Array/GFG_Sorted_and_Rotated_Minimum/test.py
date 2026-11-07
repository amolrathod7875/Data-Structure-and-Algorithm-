from Array.GFG_Sorted_and_Rotated_Minimum.code import Solution


def run_test(arr, expected):
    sol = Solution()
    result = sol.findMin(list(arr))

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: findMin({arr})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Sorted and Rotated Minimum ===\n")
run_test([5, 6, 1, 2, 3, 4], 1)
run_test([1, 2, 3, 4, 5], 1)
run_test([2, 3, 4, 5, 1], 1)
run_test([3, 4, 5, 1, 2], 1)
run_test([1], 1)
