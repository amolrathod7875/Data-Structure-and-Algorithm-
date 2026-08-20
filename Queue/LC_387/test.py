from Queue.LC_387.code import Solution


def run_test(s, expected):
    sol = Solution()
    result = sol.firstUniqChar(s)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: firstUniqChar('{s}')")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 387: First Unique Character in a String ===\n")
run_test("leetcode", 0)
run_test("loveleetcode", 2)
run_test("aabb", -1)
run_test("z", 0)
run_test("a", 0)
run_test("aa", -1)
run_test("ab", 0)
run_test("abc", 0)
run_test("aabbcc", -1)
run_test("", -1)
