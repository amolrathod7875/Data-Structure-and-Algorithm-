from Array.LC_283.code import Solution


def run_test(nums, expected):
    sol = Solution()
    original = list(nums)
    sol.moveZeroes(nums)
    result = nums

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: moveZeroes({original})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 283: Move Zeroes ===\n")
run_test([0, 1, 0, 3, 12], [1, 3, 12, 0, 0])
run_test([0], [0])
run_test([1], [1])
run_test([0, 0, 0], [0, 0, 0])
run_test([1, 2, 3], [1, 2, 3])
run_test([0, 0, 1, 2, 0, 3], [1, 2, 3, 0, 0, 0])
run_test([1, 0, 2, 0, 3, 0], [1, 2, 3, 0, 0, 0])
run_test([], [])
run_test([0, 1], [1, 0])
run_test([1, 0], [1, 0])
run_test([4, 2, 4, 0, 0, 3, 0, 5, 1, 0], [4, 2, 4, 3, 5, 1, 0, 0, 0, 0])