from Array.GFG_Count_Occurrences_in_Sorted.code import Solution


def run_test(arr, target, expected):
    sol = Solution()
    result = sol.countFreq(list(arr), target)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: countFreq({arr}, {target})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Count Occurrences in Sorted ===\n")
run_test([1, 1, 2, 2, 2, 2, 3], 2, 4)
run_test([1, 1, 2, 2, 2, 2, 3], 4, 0)
run_test([], 1, 0)
run_test([5, 5, 5, 5], 5, 4)
run_test([1, 2, 3, 4, 5], 3, 1)
