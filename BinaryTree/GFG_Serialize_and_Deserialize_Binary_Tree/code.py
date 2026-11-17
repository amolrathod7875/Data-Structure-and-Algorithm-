# Structure of binary tree node
class Node:
    def __init__(self, val=0):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def serialize(self, root):
        ans = []

        def dfs(root):
            if root is None:
                ans.append(-1)
                return
            ans.append(root.data)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ans

    def deSerialize(self, arr):
        i = [0]

        def dfs():
            if i[0] >= len(arr):
                return None
            if arr[i[0]] == -1:
                i[0] += 1
                return None
            root = Node(arr[i[0]])
            i[0] += 1
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()
