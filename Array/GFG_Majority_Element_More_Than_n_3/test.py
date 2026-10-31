from Array.GFG_Majority_Element_More_Than_n_3.code import Solution


def run_test(arr, expected):
    sol = Solution()
    result = sol.findMajority(arr)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: findMajority({arr})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Majority Element - More Than n/3 ===\n")
run_test([3, 2, 3], [3])
run_test([1], [1])
run_test([1, 2], [1, 2])
run_test([2, 2], [2])
run_test([], [])
run_test([1, 1, 1, 3, 3, 2, 2, 2], [1, 2])
run_test([1, 2, 2, 3, 2, 1, 1, 3], [1, 2])
