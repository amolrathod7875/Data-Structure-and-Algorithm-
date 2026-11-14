from BinaryTree.GFG_Two_Mirror_Trees.code import Solution


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


def run_test(v1, v2, expected):
    r1 = build_tree(v1)
    r2 = build_tree(v2)
    sol = Solution()
    result = sol.areMirror(r1, r2)

    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: areMirror({v1}, {v2})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print()


print("=== GFG: Two Mirror Trees ===\n")
run_test([1, 2, 3], [1, 3, 2], True)
run_test([1, 2, 3], [1, 2, 3], False)
run_test([], [], True)
run_test([1], [1], True)
run_test([1, 2, 3], [1, 2], False)
