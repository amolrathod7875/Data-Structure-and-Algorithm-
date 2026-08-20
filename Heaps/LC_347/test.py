import importlib.util
import sys
import os

script_dir = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("code", os.path.join(script_dir, "code.py"))
code_module = importlib.util.module_from_spec(spec)
sys.modules["code"] = code_module
spec.loader.exec_module(code_module)
Solution = code_module.Solution


def test_top_k_frequent():
    sol = Solution()
    assert sorted(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert sorted(sol.topKFrequent([1], 1)) == [1]


if __name__ == "__main__":
    test_top_k_frequent()
    print("All LC_347 tests passed.")
