from Sorting.LC_2037.code import Solution


def run_test(seats, students, expected):
    sol = Solution()
    result = sol.minMovesToSeat(seats, students)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: minMovesToSeat({seats}, {students})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 2037: Minimum Number of Moves to Seat Everyone ===\n")
run_test([3, 1, 5], [2, 7, 4], 4)
run_test([4, 1, 5, 9], [1, 3, 2, 6], 7)
run_test([2, 2, 6, 6], [1, 3, 2, 6], 4)
run_test([1], [1], 0)
run_test([2, 1, 4], [3, 1, 3], 2)
run_test([1, 2, 3], [4, 5, 6], 9)
run_test([6, 5, 4], [1, 2, 3], 9)
