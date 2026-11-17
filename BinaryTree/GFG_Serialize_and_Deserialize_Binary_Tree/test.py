from BinaryTree.GFG_Serialize_and_Deserialize_Binary_Tree.code import Solution, Node


def build_tree(values):
    if not values or values[0] is None:
        return None
    
    root = Node(values[0])
    from collections import deque
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


def tree_to_list(root):
    if root is None:
        return []
    result = []
    from collections import deque
    q = deque([root])
    while q:
        node = q.popleft()
        if node is None:
            result.append(None)
            continue
        result.append(node.data)
        q.append(node.left)
        q.append(node.right)
    # trim trailing None
    while result and result[-1] is None:
        result.pop()
    return result


def run_test(values):
    root = build_tree(values)
    sol = Solution()
    serialized = sol.serialize(root)
    deserialized = sol.deSerialize(serialized)
    result = tree_to_list(deserialized)

    status = "PASS" if result == values else "FAIL"
    print(f"{status}: serialize/deserialize({values})")
    print(f"  Serialized:   {serialized}")
    print(f"  Deserialized: {result}")
    print()


print("=== GFG: Serialize and Deserialize a Binary Tree ===\n")
run_test([1, 2, 3])
run_test([1, 2, 3, 4, 5, 6, 7])
run_test([1])
run_test([])
run_test([1, None, 2])
