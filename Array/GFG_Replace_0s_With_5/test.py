from Array.GFG_Replace_0s_With_5.code import Solution


def run_test(n, expected):
    sol = Solution()
    result = sol.convertFive(n)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: convertFive({n})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Replace All 0's With 5 ===\n")
run_test(0, 5)
run_test(1, 1)
run_test(10, 15)
run_test(100, 155)
run_test(1000, 1555)
run_test(1005, 1555)
run_test(1020, 1525)
run_test(2030, 2535)
run_test(10000, 15555)
run_test(5000, 5555)
run_test(1234, 1234)
run_test(9090, 9595)
run_test(101010, 151515)