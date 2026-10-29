import io
import sys

from Array.GFG_Array_Traversal.code import Solution


def captured(arr):
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        Solution().arrayTraversal(arr)
    finally:
        sys.stdout = old
    return buf.getvalue()


def run_test(arr, expected):
    got = captured(arr)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status}: arrayTraversal({arr})")
    print(f"  Expected: {expected!r}")
    print(f"  Got:      {got!r}")
    print()


print("=== GFG: Array Traversal ===\n")
run_test([], "")
run_test([1], "1 ")
run_test([1, 2, 3], "1 2 3 ")
run_test([10, 20, 30, 40], "10 20 30 40 ")
run_test([-1, -2, -3], "-1 -2 -3 ")
