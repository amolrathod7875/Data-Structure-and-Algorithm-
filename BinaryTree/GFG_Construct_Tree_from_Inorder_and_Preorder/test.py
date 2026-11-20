from BinaryTree.GFG_Construct_Tree_from_Inorder_and_Preorder.code import Solution, Node


def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.data] + inorder_traversal(root.right)


def preorder_traversal(root):
    if root is None:
        return []
    return [root.data] + preorder_traversal(root.left) + preorder_traversal(root.right)


def run_test(inorder, preorder, exp_in, exp_pre):
    sol = Solution()
    root = sol.buildTree(list(inorder), list(preorder))
    in_res = inorder_traversal(root)
    pre_res = preorder_traversal(root)

    status = "PASS" if (in_res == exp_in and pre_res == exp_pre) else "FAIL"
    print(f"{status}: buildTree(inorder={inorder}, preorder={preorder})")
    print(f"  Inorder:  {in_res} (expected {exp_in})")
    print(f"  Preorder: {pre_res} (expected {exp_pre})")
    print()


print("=== GFG: Construct Tree from Inorder & Preorder ===\n")
run_test([4, 2, 5, 1, 6, 3, 7], [1, 2, 4, 5, 3, 6, 7],
         [4, 2, 5, 1, 6, 3, 7], [1, 2, 4, 5, 3, 6, 7])
run_test([1], [1], [1], [1])
run_test([], [], [], [])
run_test([2, 1, 3], [1, 2, 3], [2, 1, 3], [1, 2, 3])
