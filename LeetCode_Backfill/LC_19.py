# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        if length == n :
            return head.next
        
        step_take_in = length - n - 1
        curr = head 
        
        for _ in range(step_take_in):
            curr = curr.next
        
        curr.next = curr.next.next

        return head 
        