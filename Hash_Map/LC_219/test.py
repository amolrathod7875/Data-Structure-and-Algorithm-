from Hash_Table.LC_219.code import Solution


def run_test(nums, k, expected):
    sol = Solution()
    result = sol.containsNearbyDuplicate(nums, k)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: containsNearbyDuplicate({nums}, k={k})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 219: Contains Duplicate II ===\n")
run_test([1, 2, 3, 1], 3, True)
run_test([1, 0, 1, 1], 1, True)
run_test([1, 2, 3, 1, 2, 3], 2, False)
run_test([1, 2, 3, 4, 5], 1, False)
run_test([1, 2, 3, 1], 2, False)
run_test([1], 1, False)
run_test([1, 1], 1, True)
run_test([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, False)
run_test([1, 2, 3, 4, 5, 1], 5, True)
run_test([1, 2, 3, 4, 5, 1], 4, False)
