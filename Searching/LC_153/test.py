from Searching.LC_153.code import Solution


def run_test(nums, expected):
    sol = Solution()
    result = sol.findMin(list(nums))

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: findMin({nums})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 153: Find Minimum in Rotated Sorted Array ===\n")
run_test([3,4,5,1,2], 1)
run_test([4,5,6,7,0,1,2], 0)
run_test([11,13,15,17], 11)
run_test([2,1], 1)
run_test([1], 1)
