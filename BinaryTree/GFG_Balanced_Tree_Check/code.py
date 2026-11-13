'''
# Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def isBalanced(self, root):
        
        def helper(root):
            if root is None :
                return 0
            left_node = helper(root.left)
            right_node = helper(root.right)
            
            if left_node == -1 or right_node == -1 or abs(left_node - right_node) > 1:
                return -1 
            return max(left_node, right_node) + 1 
            
        
        return helper(root) >  0
