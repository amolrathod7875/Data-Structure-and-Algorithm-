from Math.LC_4010.code import Solution


def run_test(nums, expected):
    sol = Solution()
    result = sol.maxPairStrength(nums)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: maxPairStrength({nums})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 4010: Maximize Pair Strength Using GCD ===\n")
run_test([1, 2, 3], 6)
run_test([2, 4, 8], 4)
run_test([6, 9, 15], 15)
run_test([560, 3], 1680)
run_test([2, 2], 1)
run_test([1, 1, 1], 1)
run_test([3, 5, 7, 11], 77)
run_test([620, 3], 1860)
