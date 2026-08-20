from Queue.LC_2073.code import Solution


def run_test(tickets, k, expected):
    sol = Solution()
    result = sol.timeRequiredToBuy(tickets, k)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: timeRequiredToBuy({tickets}, k={k})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 2073: Time Needed to Buy Tickets ===\n")
run_test([2, 3, 2], 2, 6)
run_test([5, 1, 1, 1], 0, 8)
run_test([1, 2, 3], 0, 1)
run_test([1, 2, 3], 1, 4)
run_test([1, 2, 3], 2, 6)
run_test([1], 0, 1)
run_test([2, 2, 2], 0, 4)
run_test([3, 3, 3], 1, 8)
run_test([2, 3, 2], 0, 4)
