from Stack.LC_496.code import Solution


def run_test(nums1, nums2, expected):
    sol = Solution()
    result = sol.nextGreaterElement(nums1, nums2)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: nextGreaterElement({nums1}, {nums2})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 496: Next Greater Element I ===\n")
run_test([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1])
run_test([2, 4], [1, 2, 3, 4], [3, -1])
run_test([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7], [7, 7, 7, 7, 7])
run_test([1], [1], [-1])
run_test([], [1, 2], [])
