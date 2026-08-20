class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = ListNode()   # left sentinel
        self.tail = ListNode()   # right sentinel
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        # Optimization: choose shorter direction
        if index < self.size / 2:
            cur = self.head.next
            for _ in range(index):
                cur = cur.next
        else:
            cur = self.tail.prev
            for _ in range(self.size - 1 - index):
                cur = cur.prev
        return cur.val

    def addAtHead(self, val):
        self._insert(self.head, val)

    def addAtTail(self, val):
        self._insert(self.tail.prev, val)

    def addAtIndex(self, index, val):
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
        else:
            prev = self._getNode(index - 1)
            self._insert(prev, val)

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        target = self._getNode(index)
        target.prev.next = target.next
        target.next.prev = target.prev
        self.size -= 1

    def _insert(self, prev_node, val):
        """Insert val AFTER prev_node"""
        new_node = ListNode(val, prev_node, prev_node.next)
        prev_node.next.prev = new_node
        prev_node.next = new_node
        self.size += 1

    def _getNode(self, index):
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        return cur