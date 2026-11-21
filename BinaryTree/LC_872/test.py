from BinaryTree.LC_872.code import Solution, TreeNode


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
    r1 = build_tree(v1)
    r2 = build_tree(v2)
    sol = Solution()
    result = sol.leafSimilar(r1, r2)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: leafSimilar({v1}, {v2})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 872: Leaf-Similar Trees ===\n")
run_test([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4],
         [3, 1, 5, 8, 9, 6, 7, 4, 2], False)
run_test([1], [1], True)
run_test([1], [2], False)
run_test([], [], True)
run_test([1, 2, 3], [1, 3, 2], False)
run_test([1, 2, 3], [1, 2, 3], True)
