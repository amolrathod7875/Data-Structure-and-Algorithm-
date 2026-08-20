from Hash_Map.LC_3731.code import Solution


def run_test(nums, expected):
    sol = Solution()
    result = sol.findMissingElements(nums)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: findMissingElements({nums})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 3731: Find Missing Elements ===\n")
run_test([1, 4, 2, 5], [3])
run_test([7, 8, 6, 9], [])
run_test([5, 1], [2, 3, 4])
run_test([1, 2, 3, 4, 5], [])
run_test([10, 12, 15, 11], [13, 14])
run_test([1, 3], [2])
run_test([1, 100], list(range(2, 100)))
