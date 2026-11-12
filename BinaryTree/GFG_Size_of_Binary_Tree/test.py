import importlib.util
import sys
import os

script_dir = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("code", os.path.join(script_dir, "code.py"))
code_module = importlib.util.module_from_spec(spec)
sys.modules["code"] = code_module
spec.loader.exec_module(code_module)
Solution = code_module.Solution
Node = code_module.Node


def test_getSize():
    sol = Solution()
    # Empty tree
    assert sol.getSize(None) == 0
    # Single node
    root1 = Node(1)
    assert sol.getSize(root1) == 1
    # Tree with two children
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    assert sol.getSize(root2) == 3
    # Skewed tree
    root3 = Node(1)
    root3.right = Node(2)
    root3.right.right = Node(3)
    assert sol.getSize(root3) == 3

if __name__ == "__main__":
    test_getSize()
    print("All GFG_Size_of_Binary_Tree tests passed.")