from Array.LC_1929.code import Solution


def run_test(nums, expected):
    sol = Solution()
    result = sol.getConcatenation(nums)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: getConcatenation({nums})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 1929: Concatenation of Array ===\n")
run_test([1, 2, 1], [1, 2, 1, 1, 2, 1])
run_test([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1])
run_test([1], [1, 1])
run_test([5, 6, 7, 8, 9], [5, 6, 7, 8, 9, 5, 6, 7, 8, 9])
run_test([10], [10, 10])
run_test([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6])
