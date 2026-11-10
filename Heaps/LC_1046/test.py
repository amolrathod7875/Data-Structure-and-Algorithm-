import importlib.util
import sys
import os

script_dir = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("code", os.path.join(script_dir, "code.py"))
code_module = importlib.util.module_from_spec(spec)
sys.modules["code"] = code_module
spec.loader.exec_module(code_module)
Solution = code_module.Solution


def test_lastStoneWeight():
    sol = Solution()
    assert sol.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert sol.lastStoneWeight([1, 3, 7, 1]) == 2
    assert sol.lastStoneWeight([10, 4, 2, 10]) == 2


if __name__ == "__main__":
    test_lastStoneWeight()
    print("All LC_1046 tests passed.")