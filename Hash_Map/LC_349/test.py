from Hash_Map.LC_349.code import Solution


def run_test(nums1, nums2, expected):
    sol = Solution()
    result = sorted(sol.intersection(nums1, nums2))

    status = "PASS" if result == sorted(expected) else "FAIL"
    print(f"{status}: intersection({nums1}, {nums2})")
    print(f"  Expected: {sorted(expected)}")
    print(f"  Got:      {result}")
    print()


print("=== LC 349: Intersection of Two Arrays ===\n")
run_test([1, 2, 2, 1], [2, 2], [2])
run_test([4, 9, 5], [9, 4, 9, 8, 4], [9, 4])
run_test([1, 2, 3], [4, 5, 6], [])
run_test([1, 1, 1, 1], [1, 1], [1])
run_test([1, 2, 3, 4], [2, 3, 4, 5], [2, 3, 4])
run_test([], [1, 2], [])
run_test([1, 2], [], [])
