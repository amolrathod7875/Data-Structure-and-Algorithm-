from Array.LC_1011.code import Solution


def run_test(weights, days, expected):
    sol = Solution()
    result = sol.shipWithinDays(list(weights), days)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: shipWithinDays({weights}, {days})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 1011: Capacity To Ship Packages Within D Days ===\n")
run_test([1,2,3,4,5,6,7,8,9,10], 5, 15)
run_test([3,2,2,4,1,4], 3, 6)
run_test([1,2,3,1,1], 4, 3)
run_test([1], 1, 1)
