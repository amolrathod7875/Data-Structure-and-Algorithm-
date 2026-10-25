from Array.LC_1470.code import Solution


def run_test(nums, n, expected):
    sol = Solution()
    result = sol.shuffle(nums, n)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: shuffle({nums}, {n})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 1470: Shuffle the Array ===\n")
run_test([2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7])
run_test([1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1])
run_test([1, 1, 2, 2], 2, [1, 2, 1, 2])
run_test([0, 0, 0, 0], 2, [0, 0, 0, 0])
