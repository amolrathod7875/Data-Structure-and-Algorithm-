from Array.LC_3925.code import Solution


def run_test(nums, expected):
    sol = Solution()
    result = sol.concatenateArray(nums)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: concatenateArray({nums})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 3925: Concatenate Array With Reverse ===\n")
run_test([1, 2, 3], [1, 2, 3, 3, 2, 1])
run_test([1, 2, 3, 4], [1, 2, 3, 4, 4, 3, 2, 1])
run_test([1], [1, 1])
run_test([5, 6], [5, 6, 6, 5])
run_test([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 5, 4, 3, 2, 1])
run_test([], [])
