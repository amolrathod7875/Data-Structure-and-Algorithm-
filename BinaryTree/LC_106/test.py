from BinaryTree.LC_106.code import Solution, TreeNode


def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


def postorder_traversal(root):
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]


def run_test(inorder, postorder, exp_in, exp_post):
    sol = Solution()
    root = sol.buildTree(list(inorder), list(postorder))
    in_res = inorder_traversal(root)
    post_res = postorder_traversal(root)

    status = "PASS" if (in_res == exp_in and post_res == exp_post) else "FAIL"
    print(f"{status}: buildTree(inorder={inorder}, postorder={postorder})")
    print(f"  Inorder:   {in_res} (expected {exp_in})")
    print(f"  Postorder: {post_res} (expected {exp_post})")
    print()


print("=== LC 106: Construct Binary Tree from Inorder and Postorder Traversal ===\n")
run_test([9, 3, 15, 20, 7], [9, 15, 7, 20, 3],
         [9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
run_test([-1], [-1], [-1], [-1])
run_test([], [], [], [])
run_test([2, 1, 3], [2, 3, 1], [2, 1, 3], [2, 3, 1])
