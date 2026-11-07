from Searching.LC_33.code import Solution


def run_test(nums, target, expected):
    sol = Solution()
    result = sol.search(list(nums), target)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: search({nums}, {target})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 33: Search in Rotated Sorted Array ===\n")
run_test([4,5,6,7,0,1,2], 0, 4)
run_test([4,5,6,7,0,1,2], 3, -1)
run_test([1], 0, -1)
run_test([3,1], 1, 1)
