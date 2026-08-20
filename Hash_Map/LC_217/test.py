from Hash_Map.LC_217.code import Solution


def run_test(nums, expected):
    sol = Solution()
    result = sol.containsDuplicate(nums)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: containsDuplicate({nums})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 217: Contains Duplicate ===\n")
run_test([1, 2, 3, 1], True)
run_test([1, 2, 3, 4], False)
run_test([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)
run_test([1], False)
run_test([1, 2], False)
run_test([2, 2], True)
run_test([], False)
run_test([100, 200, 300, 100], True)
