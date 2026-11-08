from code import isMaxHeap


def run_tests(description, actual, expected):
    status = "Pass" if actual == expected else "fail"
    print(f"{status} : {description}")
    if status == "fail":
        print(f"    Expected: {expected}")
        print(f"    Got: {actual}")
    print()


print("=== isMaxHeap Tests ===\n")

# Valid max heap arrays
run_tests("Valid max heap with 6 elements", isMaxHeap([90, 15, 10, 7, 12, 2]), True)
run_tests("Valid max heap with 7 elements", isMaxHeap([100, 90, 80, 70, 60, 50, 40]), True)
run_tests("Single element is max heap", isMaxHeap([5]), True)
run_tests("Two elements in max heap order", isMaxHeap([10, 5]), True)
run_tests("Empty array is max heap", isMaxHeap([]), True)

# Invalid max heap arrays
run_tests("Invalid: parent < left child", isMaxHeap([9, 15, 10, 7, 12, 11]), False)
run_tests("Invalid: parent < right child", isMaxHeap([100, 90, 50, 80, 60, 55, 40]), False)
run_tests("Invalid: root smaller than child", isMaxHeap([5, 10, 3]), False)
run_tests("Invalid: deep violation at leaf parent", isMaxHeap([100, 90, 80, 70, 60, 55, 40, 30, 20, 10, 65]), False)

# Edge cases with odd/even lengths
run_tests("Even length valid heap", isMaxHeap([10, 9, 8, 7, 6, 5]), True)
run_tests("Odd length valid heap", isMaxHeap([10, 9, 8, 7, 6, 5, 4]), True)
run_tests("Even length invalid heap", isMaxHeap([10, 9, 11, 7, 6, 5]), False)
run_tests("Odd length invalid heap", isMaxHeap([10, 9, 8, 7, 11, 5, 4]), False)
