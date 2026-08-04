from Hash_Map.LC_242.code import Solution


def run_test(s, t, expected):
    sol = Solution()
    result = sol.isAnagram(s, t)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: isAnagram('{s}', '{t}')")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 242: Valid Anagram ===\n")
run_test("anagram", "nagaram", True)
run_test("rat", "car", False)
run_test("a", "a", True)
run_test("a", "b", False)
run_test("ab", "ba", True)
run_test("ab", "ac", False)
run_test("", "", True)
run_test("aabbcc", "ccbbaa", True)
run_test("aabbcc", "ccbbaaa", False)
run_test("listen", "silent", True)
