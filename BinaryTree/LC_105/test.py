from BinaryTree.LC_105.code import Solution, TreeNode


def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


def preorder_traversal(root):
    if root is None:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


def run_test(preorder, inorder, exp_pre, exp_in):
    sol = Solution()
    root = sol.buildTree(list(preorder), list(inorder))
    pre_res = preorder_traversal(root)
    in_res = inorder_traversal(root)

    status = "PASS" if (pre_res == exp_pre and in_res == exp_in) else "FAIL"
    print(f"{status}: buildTree(preorder={preorder}, inorder={inorder})")
    print(f"  Preorder: {pre_res} (expected {exp_pre})")
    print(f"  Inorder:  {in_res} (expected {exp_in})")
    print()


print("=== LC 105: Construct Binary Tree from Preorder and Inorder Traversal ===\n")
run_test([3, 9, 20, 15, 7], [9, 3, 15, 20, 7],
         [3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
run_test([-1], [-1], [-1], [-1])
run_test([], [], [], [])
run_test([1, 2, 3], [2, 1, 3], [1, 2, 3], [2, 1, 3])
