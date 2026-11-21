from BinaryTree.LC_111.code import Solution, TreeNode


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
    result = sol.minDepth(root)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: minDepth({values})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 111: Minimum Depth of Binary Tree ===\n")
run_test([3, 9, 20, None, None, 15, 7], 2)
run_test([2, None, 3, None, 4, None, 5, None, 6], 5)
run_test([1], 1)
run_test([], 0)
run_test([1, 2, 3, 4, 5, 6, 7], 3)
