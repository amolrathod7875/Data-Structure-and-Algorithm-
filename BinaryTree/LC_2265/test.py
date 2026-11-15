from BinaryTree.LC_2265.code import Solution, TreeNode


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


def run_test(values, expected):
    root = build_tree(values)
    sol = Solution()
    result = sol.averageOfSubtree(root)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: averageOfSubtree({values})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 2265: Count Nodes Equal to Average of Subtree ===\n")
run_test([4, 8, 5, 0, 1, None, 6], 5)
run_test([1], 1)
run_test([], 0)
run_test([2, 4, 6, None, None, 2, 3], 3)
