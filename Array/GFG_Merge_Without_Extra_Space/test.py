from Array.GFG_Merge_Without_Extra_Space.code import Solution


def run_test(a, b, exp_a, exp_b):
    sol = Solution()
    aa, bb = list(a), list(b)
    sol.mergeArrays(aa, bb)

    status = "PASS" if (aa == exp_a and bb == exp_b) else "FAIL"
    print(f"{status}: mergeArrays({a}, {b})")
    print(f"  Expected a: {exp_a}, b: {exp_b}")
    print(f"  Got      a: {aa}, b: {bb}")
    print()


print("=== GFG: Merge Without Extra Space ===\n")
run_test([1, 3, 5, 7], [2, 4, 6, 8], [1, 2, 3, 4], [5, 6, 7, 8])
run_test([1, 2, 3], [4, 5], [1, 2, 3], [4, 5])
run_test([10, 12], [5, 6, 7], [5, 6], [7, 10, 12])
run_test([], [1, 2], [], [1, 2])
run_test([1, 2], [], [1, 2], [])
