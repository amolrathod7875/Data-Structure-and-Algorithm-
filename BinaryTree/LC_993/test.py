from BinaryTree.LC_993.code import Solution, TreeNode


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


def run_test(values, x, y, expected):
    root = build_tree(values)
    sol = Solution()
    result = sol.isCousins(root, x, y)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: isCousins({values}, {x}, {y})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 993: Cousins in Binary Tree ===\n")
run_test([1, 2, 3, 4], 4, 3, False)
run_test([1, 2, 3, None, 4, None, 5], 5, 4, True)
run_test([1, 2, 3], 2, 3, False)
run_test([1], 1, 2, False)
run_test([], 1, 2, False)
