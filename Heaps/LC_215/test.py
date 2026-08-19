import importlib.util
import sys
import os

script_dir = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("code", os.path.join(script_dir, "code.py"))
code_module = importlib.util.module_from_spec(spec)
sys.modules["code"] = code_module
spec.loader.exec_module(code_module)
Solution = code_module.Solution


def test_find_kth_largest():
    sol = Solution()
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


if __name__ == "__main__":
    test_find_kth_largest()
    print("All LC_215 tests passed.")
