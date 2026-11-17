from BinaryTree.LC_297.code import Codec, TreeNode


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
        result.append(node.val)
        q.append(node.left)
        q.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


def run_test(values):
    root = build_tree(values)
    codec = Codec()
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    result = tree_to_list(deserialized)

    status = "PASS" if result == values else "FAIL"
    print(f"{status}: serialize/deserialize({values})")
    print(f"  Serialized:   {serialized}")
    print(f"  Deserialized: {result}")
    print()


print("=== LC 297: Serialize and Deserialize Binary Tree ===\n")
run_test([1, 2, 3])
run_test([1, 2, 3, 4, 5, 6, 7])
run_test([1])
run_test([])
run_test([1, None, 2])
