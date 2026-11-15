from BinaryTree.GFG_Sum_Tree.code import Solution


def build_tree(values):
    if not values or values[0] is None:
        return None
    
    class Node:
        def __init__(self, val):
            self.data = val
            self.left = None
            self.right = None
    
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
    result = sol.isSumTree(root)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: isSumTree({values})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Sum Tree ===\n")
# Leaf only
run_test([10], True)
# Sum tree: root = left+right
run_test([10, 4, 6], True)
run_test([26, 10, 3, 4, 6, None, 3], True)
# Not sum tree
run_test([10, 4, 5], False)
run_test([1, 2, 3], False)
# Empty
run_test([], True)
