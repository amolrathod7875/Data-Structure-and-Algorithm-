from BinaryTree.GFG_Sum_Nodes_on_Longest_Path.code import Solution, Node


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
    result = sol.sumOfLongRootToLeafPath(root)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: sumOfLongRootToLeafPath({values})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Sum Nodes on Longest Path ===\n")
run_test([4, 2, 5, 7, 1, 2, 3, None, None, 6], 13)
run_test([4, 2, 5, 7, 1, 2, 3], 13)
run_test([1], 1)
run_test([], 0)
