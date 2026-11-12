import importlib.util
import sys
import os

script_dir = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("code", os.path.join(script_dir, "code.py"))
code_module = importlib.util.module_from_spec(spec)
sys.modules["code"] = code_module
spec.loader.exec_module(code_module)
Solution = code_module.Solution
TreeNode = code_module.TreeNode


def test_countNodes():
    sol = Solution()
    # Example 1: tree with nodes 1-6
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    assert sol.countNodes(root1) == 6

    # Example 2: empty tree
    assert sol.countNodes(None) == 0

    # Example 3: single node
    root3 = TreeNode(1)
    assert sol.countNodes(root3) == 1

if __name__ == "__main__":
    test_countNodes()
    print("All LC_222 tests passed.")