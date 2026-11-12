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


def test_height():
    sol = Solution()
    # Empty tree
    assert sol.height(None) == -1
    # Single node
    root1 = Node(1)
    assert sol.height(root1) == 0
    # Balanced tree of height 2
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
    root2.right.left = Node(6)
    root2.right.right = Node(7)
    assert sol.height(root2) == 2
    # Skewed tree of height 2
    root3 = Node(1)
    root3.right = Node(2)
    root3.right.right = Node(3)
    assert sol.height(root3) == 2

if __name__ == "__main__":
    test_height()
    print("All GFG_Height_of_Binary_Tree tests passed.")