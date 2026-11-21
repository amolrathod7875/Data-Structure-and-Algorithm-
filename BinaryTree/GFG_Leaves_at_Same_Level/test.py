from BinaryTree.GFG_Leaves_at_Same_Level.code import Solution, Node


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
    result = sol.check(root)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: check({values})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Leaves at Same Level or Not ===\n")
run_test([1, 2, 3], True)
run_test([1, 2, 3, 4, 5, 6, 7], True)
run_test([1, 2, 3, 4, None, 5, 6], True)
run_test([1, 2, 3, 4, 5, 6, 7, 8], False)
run_test([1], True)
run_test([], True)
