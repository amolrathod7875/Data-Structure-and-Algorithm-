from BinaryTree.LC_257.code import Solution, TreeNode


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
    result = sol.binaryTreePaths(root)
    result_sorted = sorted(result)
    expected_sorted = sorted(expected)

    status = "PASS" if result_sorted == expected_sorted else "FAIL"
    print(f"{status}: binaryTreePaths({values})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== LC 257: Binary Tree Paths ===\n")
run_test([1, 2, 3, None, 5], ["1->2->5", "1->3"])
run_test([1], ["1"])
run_test([], [])
