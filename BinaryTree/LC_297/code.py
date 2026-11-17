# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        ans = []

        def dfs(root):
            if root is None:
                ans.append("None")
                return

            ans.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(ans)

    def deserialize(self, data):
        arr = data.split(",")
        i = 0

        def dfs():
            nonlocal i

            if arr[i] == "None":
                i += 1
                return None

            root = TreeNode(int(arr[i]))
            i += 1

            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()
