# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        write = head
        curr = head.next 
        total = 0 
        while curr :
            if curr.val == 0:
                write.next = curr
                write = curr
                write.val = total
                total = 0
            else:
                total += curr.val
            curr = curr.next
        write.next = None
        return head.next