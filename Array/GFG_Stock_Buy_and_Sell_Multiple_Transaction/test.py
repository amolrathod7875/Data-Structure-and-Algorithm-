from Array.GFG_Stock_Buy_and_Sell_Multiple_Transaction.code import Solution


def run_test(prices, expected):
    sol = Solution()
    result = sol.maxProfit(prices)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: maxProfit({prices})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Stock Buy and Sell – Multiple Transaction ===\n")
run_test([100, 180, 260, 310, 40, 535, 695], 865)
run_test([4, 2, 2, 2, 4], 2)
run_test([1], 0)
run_test([], 0)
run_test([1, 2, 3, 4, 5], 4)
run_test([5, 4, 3, 2, 1], 0)
