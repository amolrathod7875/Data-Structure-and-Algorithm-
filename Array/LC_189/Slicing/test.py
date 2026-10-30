from Array.LC_189.Slicing.code import Solution


def run_test(nums, k, expected):
    sol = Solution()
    original = list(nums)
    sol.rotate(nums, k)
    result = nums

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: rotate({original}, {k})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 189: Rotate Array (Slicing) ===\n")
run_test([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4])
run_test([-1, -100, 3, 99], 2, [3, 99, -1, -100])
run_test([1, 2, 3], 0, [1, 2, 3])
run_test([1, 2, 3], 3, [1, 2, 3])
run_test([1, 2, 3], 4, [3, 1, 2])
run_test([1, 2, 3, 4, 5], 7, [4, 5, 1, 2, 3])
run_test([1], 0, [1])
run_test([1], 5, [1])
run_test([], 3, [])
run_test([1, 1, 2, 2, 3, 3], 2, [2, 2, 3, 3, 1, 1])
run_test([1, 2, 3, 4, 5, 6], 2, [5, 6, 1, 2, 3, 4])
run_test([2, 3, 4, 5, 6, 7], 1, [7, 2, 3, 4, 5, 6])