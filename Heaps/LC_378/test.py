import importlib.util
import sys
import os

script_dir = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("code", os.path.join(script_dir, "code.py"))
code_module = importlib.util.module_from_spec(spec)
sys.modules["code"] = code_module
spec.loader.exec_module(code_module)
Solution = code_module.Solution


def test_kth_smallest():
    sol = Solution()
    assert sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8) == 13
    assert sol.kthSmallest([[-5]], 1) == -5

if __name__ == "__main__":
    test_kth_smallest()
    print("All LC_378 tests passed.")