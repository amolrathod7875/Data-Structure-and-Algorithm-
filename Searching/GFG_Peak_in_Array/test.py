from Searching.GFG_Peak_in_Array.code import Solution


def run_test(arr, expected_index):
    sol = Solution()
    idx = sol.peakElement(list(arr))
    # verify it's a peak
    is_peak = (idx == 0 or arr[idx] >= arr[idx-1]) and (idx == len(arr)-1 or arr[idx] >= arr[idx+1])
    status = "PASS" if (idx == expected_index or is_peak) else "FAIL"
    print(f"{status}: peakElement({arr}) -> index {idx} (value {arr[idx]})")
    print(f"  Expected index: {expected_index}")
    print()


print("=== GFG: Peak in Array ===\n")
run_test([1, 2, 3], 2)
run_test([1, 2, 3, 1], 2)
run_test([5, 10, 20, 15], 2)
run_test([10, 20, 15, 2, 23, 90, 67], 1)
run_test([1], 0)
run_test([1, 2], 1)
