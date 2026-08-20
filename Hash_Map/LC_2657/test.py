from Hash_Map.LC_2657.code import Solution


def run_test(A, B, expected):
    sol = Solution()
    result = sol.findPrefixCommonArray(A, B)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: findPrefixCommonArray({A}, {B})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 2657: Find the Prefix Common Array of Two Arrays ===\n")
run_test([1, 3, 2, 4], [3, 1, 2, 4], [0, 2, 3, 4])
run_test([1, 2, 3, 4], [2, 3, 4, 1], [0, 1, 2, 4])
run_test([1, 2], [1, 2], [1, 2])
run_test([2, 1], [1, 2], [0, 2])
run_test([1, 2, 3], [1, 2, 3], [1, 2, 3])
run_test([3, 1, 2], [2, 3, 1], [0, 1, 3])
