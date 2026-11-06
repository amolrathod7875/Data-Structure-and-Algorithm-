from Array.GFG_Ceil_in_Sorted_Array.code import Solution


def run_test(arr, x, expected):
    sol = Solution()
    r1 = sol.findCeil(list(arr), x)
    r2 = sol.findCeilNaive(list(arr), x)

    s1 = "PASS" if r1 == expected else "FAIL"
    s2 = "PASS" if r2 == expected else "FAIL"
    print(f"{s1}: findCeil({arr}, {x}) -> {r1} (expected {expected})")
    print(f"{s2}: findCeilNaive({arr}, {x}) -> {r2} (expected {expected})")
    print()


print("=== GFG: Ceil in Sorted Array ===\n")
run_test([1, 2, 8, 10, 10, 12, 19], 5, 2)
run_test([1, 2, 8, 10, 10, 12, 19], 20, -1)
run_test([1, 2, 8, 10, 10, 12, 19], 0, 0)
run_test([1, 1, 2, 3, 4], 2, 2)
run_test([], 5, -1)
