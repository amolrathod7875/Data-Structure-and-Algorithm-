from Array.LC_81.code import Solution


def run_test(nums, target, expected):
    sol = Solution()
    result = sol.search(list(nums), target)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: search({nums}, {target})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 81: Search in Rotated Sorted Array II ===\n")
run_test([2,5,6,0,0,1,2], 0, True)
run_test([2,5,6,0,0,1,2], 3, False)
run_test([1,0,1,1,1], 0, True)
run_test([1], 0, False)
run_test([], 0, False)
