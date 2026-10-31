from Array.LC_229.code import Solution


def run_test(nums, expected):
    sol = Solution()
    result = sol.majorityElement(nums)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: majorityElement({nums})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 229: Majority Element II ===\n")
run_test([3, 2, 3], [3])
run_test([1], [1])
run_test([1, 2], [1, 2])
run_test([], [])
run_test([1, 1, 1, 3, 3, 2, 2, 2], [1, 2])
run_test([2, 2], [2])
