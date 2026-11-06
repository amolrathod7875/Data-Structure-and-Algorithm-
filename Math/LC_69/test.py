from Math.LC_69.code import Solution


def run_test(x, expected):
    sol = Solution()
    result = sol.mySqrt(x)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: mySqrt({x})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 69: Sqrt(x) ===\n")
run_test(0, 0)
run_test(1, 1)
run_test(4, 2)
run_test(8, 2)
run_test(9, 3)
run_test(2147483647, 46340)
