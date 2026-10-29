from Array.LC_2460.code import Solution


def run_test(nums, expected):
    sol = Solution()
    original = list(nums)
    result = sol.applyOperations(nums)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: applyOperations({original})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 2460: Apply Operations to an Array ===\n")
run_test([1, 2, 2, 1, 1, 0], [1, 4, 2, 0, 0, 0])
run_test([0, 1], [1, 0])
run_test([2, 2, 2, 2], [4, 4, 0, 0])
run_test([1, 2, 3, 4], [1, 2, 3, 4])
run_test([0, 0, 0, 0], [0, 0, 0, 0])
run_test([5], [5])
run_test([1, 1, 1, 1, 1], [2, 2, 1, 0, 0])
run_test([3, 3, 3, 3, 3, 3], [6, 6, 6, 0, 0, 0])
run_test([1, 2, 2, 2, 2], [1, 4, 4, 0, 0])
run_test([2, 1, 1, 2, 2], [2, 2, 4, 0, 0])