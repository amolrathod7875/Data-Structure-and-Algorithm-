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


def test_maxDepth():
    sol = Solution()
    # Example 1 tree: [3,9,20,null,null,15,7]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    assert sol.maxDepth(root1) == 3

    # Example 2 tree: [1,null,2]
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    assert sol.maxDepth(root2) == 2

    # Empty tree
    assert sol.maxDepth(None) == 0

if __name__ == "__main__":
    test_maxDepth()
    print("All LC_104 tests passed.")