from BinaryTree.GFG_Left_View_of_Binary_Tree.code import Solution


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
    result = sol.leftView(root)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: leftView({values})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Left View of Binary Tree ===\n")
run_test([1, 2, 3, 4, 5, 6, 7], [1, 2, 4])
run_test([1, 2, 3, None, None, 4, 5], [1, 2, 4])
run_test([1], [1])
run_test([], [])
