from Array.GFG_Stock_Buy_and_Sell_Max_One_Transaction.code import Solution


def run_test(prices, expected):
    sol = Solution()
    result = sol.maxProfit(prices)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: maxProfit({prices})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Stock Buy and Sell – Max One Transaction ===\n")
run_test([7, 1, 5, 3, 6, 4], 5)
run_test([7, 6, 4, 3, 1], 0)
run_test([1], 0)
run_test([], 0)
run_test([2, 4, 1], 2)
run_test([3, 3, 5, 0, 0, 3, 1, 4], 4)
