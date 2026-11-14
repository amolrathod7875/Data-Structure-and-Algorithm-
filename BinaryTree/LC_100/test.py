from BinaryTree.LC_100.code import Solution, TreeNode


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


def run_test(v1, v2, expected):
    p = build_tree(v1)
    q = build_tree(v2)
    sol = Solution()
    result = sol.isSameTree(p, q)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: isSameTree({v1}, {v2})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 100: Same Tree ===\n")
run_test([1, 2, 3], [1, 2, 3], True)
run_test([1, 2], [1, None, 2], False)
run_test([1, 2, 1], [1, 1, 2], False)
run_test([], [], True)
run_test([1], [1], True)
