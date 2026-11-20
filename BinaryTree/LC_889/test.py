from BinaryTree.LC_889.code import Solution, TreeNode


def preorder_traversal(root):
    if root is None:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


def postorder_traversal(root):
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]


def run_test(preorder, postorder, exp_pre, exp_post):
    sol = Solution()
    root = sol.constructFromPrePost(list(preorder), list(postorder))
    pre_res = preorder_traversal(root)
    post_res = postorder_traversal(root)

    status = "PASS" if (pre_res == exp_pre and post_res == exp_post) else "FAIL"
    print(f"{status}: constructFromPrePost(preorder={preorder}, postorder={postorder})")
    print(f"  Preorder:  {pre_res} (expected {exp_pre})")
    print(f"  Postorder: {post_res} (expected {exp_post})")
    print()


print("=== LC 889: Construct Binary Tree from Preorder and Postorder Traversal ===\n")
run_test([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1],
         [1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1])
run_test([-1], [-1], [-1], [-1])
run_test([], [], [], [])
run_test([1, 2, 3], [2, 3, 1], [1, 2, 3], [2, 3, 1])
