from Hash_Map.LC_1832.code import Solution


def run_test(sentence, expected):
    sol = Solution()
    result = sol.checkIfPangram(sentence)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: checkIfPangram('{sentence}')")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 1832: Check if the Sentence Is Pangram ===\n")
run_test("thequickbrownfoxjumpsoverthelazydog", True)
run_test("leetcode", False)
run_test("abcdefghijklmnopqrstuvwxyz", True)
run_test("thequickbrownfoxjumpsoverthe", False)
run_test("a", False)
run_test("", False)
run_test("abcdefghijklmnopqrstuvwxy", False)
run_test("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", True)
