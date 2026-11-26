# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            g = gcd(curr.val, curr.next.val)
            new_node = ListNode(g, curr.next)
            curr.next = new_node
            curr = new_node.next
        return head

        