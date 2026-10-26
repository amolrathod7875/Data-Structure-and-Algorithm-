from Array.LC_215.code import Solution


def run_test(nums, k, expected):
    sol = Solution()
    original = list(nums)
    result = sol.findKthLargest(nums, k)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: findKthLargest({original}, {k})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 215: Kth Largest Element in an Array ===\n")
run_test([3, 2, 1, 5, 6, 4], 2, 5)
run_test([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4)
run_test([1], 1, 1)
run_test([1, 2], 1, 2)
run_test([1, 2], 2, 1)
run_test([5, 5, 5, 5], 2, 5)
run_test([-1, -3, -2, -5, 0], 2, -1)
run_test([7, 6, 5, 4, 3, 2, 1], 3, 5)
run_test([10, 20, 30, 40, 50], 1, 50)
run_test([10, 20, 30, 40, 50], 5, 10)