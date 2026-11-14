'''
# Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def areMirror(self, a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.data != b.data:
            return False
        return (self.areMirror(a.left, b.right) and
                self.areMirror(a.right, b.left))
