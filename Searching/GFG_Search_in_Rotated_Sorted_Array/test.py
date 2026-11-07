from Searching.GFG_Search_in_Rotated_Sorted_Array.code import Solution


def run_test(arr, key, expected):
    sol = Solution()
    result = sol.search(list(arr), key)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: search({arr}, {key})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Search in Rotated Sorted Array ===\n")
run_test([5, 6, 7, 8, 9, 10, 1, 2, 3], 3, 8)
run_test([5, 6, 7, 8, 9, 10, 1, 2, 3], 10, 5)
run_test([5, 6, 7, 8, 9, 10, 1, 2, 3], 11, -1)
run_test([1], 0, -1)
run_test([1, 3], 3, 1)
