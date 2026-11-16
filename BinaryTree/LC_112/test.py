from BinaryTree.LC_112.code import Solution, TreeNode


def build_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    from collections import deque
    q = deque([root])
    idx = 1
    while q and idx < len(values):
        node = q.popleft()
        if values[idx] is not None:
            node.left = TreeNode(values[idx])
            q.append(node.left)
        idx += 1
        if idx < len(values) and values[idx] is not None:
            node.right = TreeNode(values[idx])
            q.append(node.right)
        idx += 1
    return root


def run_test(values, target, expected):
    root = build_tree(values)
    sol = Solution()
    result = sol.hasPathSum(root, target)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: hasPathSum({values}, {target})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 112: Path Sum ===\n")
run_test([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True)
run_test([1, 2, 3], 5, False)
run_test([1, 2], 3, True)
run_test([1], 1, True)
run_test([], 0, False)
