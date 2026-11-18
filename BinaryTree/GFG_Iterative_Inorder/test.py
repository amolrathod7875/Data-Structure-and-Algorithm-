from BinaryTree.GFG_Iterative_Inorder.code import Solution, Node


def build_tree(values):
    if not values or values[0] is None:
        return None

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
    result = sol.inOrder(root)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: inOrder({values})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Iterative Inorder ===\n")
run_test([1, 2, 3, 4, 5, 6, 7], [4, 2, 5, 1, 6, 3, 7])
run_test([1, None, 2, None, 3], [1, 2, 3])
run_test([1], [1])
run_test([], [])
