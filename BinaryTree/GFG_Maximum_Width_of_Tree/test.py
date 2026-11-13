from BinaryTree.GFG_Maximum_Width_of_Tree.code import Solution


def build_tree(values):
    if not values:
        return None
    from BinaryTree.GFG_Maximum_Width_of_Tree.code import Node
    root = Node(values[0])
    from collections import deque
    q = deque([root])
    idx = 1
    while q and idx < len(values):
        node = q.popleft()
        if values[idx] is not None:
            node.left = Node(values[idx])
            q.append(node.left)
        idx += 1
        if idx < len(values) and values[idx] is not None:
            node.right = Node(values[idx])
            q.append(node.right)
        idx += 1
    return root


def run_test(values, expected):
    root = build_tree(values)
    sol = Solution()
    result = sol.maxWidth(root)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: maxWidth({values})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Maximum Width of Binary Tree ===\n")
run_test([1, 3, 2], 2)
run_test([1, 3, 2, 5, 3, None, 9], 4)
run_test([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, 12, None, None, 15], 5)
run_test([], 0)
