class Node:
    def __init__(self,data):
        self.data = data 
        self.prev = None
        self.next = None 

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return new_node

    def remove_node(self,node):
        if node is None:
            return 

        if node == self.head:
            self.head = node.next

        if node == self.tail:
            self.tail = node.prev

        if node.prev:
            node.prev.next = node.next

        node.prev = None
        node.next = None

    def insert_before(self, new_node, existing_node):

        if new_node is None or existing_node is None:
            return 

        if new_node.prev is not None or new_node.next is not None:
            self.remove_node(new_node)

        new_node.next = existing_node
        new_node.prev = existing_node.prev
        existing_node.prev = new_node

        if new_node.prev:
            new_node.prev.next = new_node
        else:
            self.head = new_node

    def display_forward(self):
        elements= []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" <-> ".join(elements) if elements else "Empty List")

    def display_backword(self):
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.data))
            current = current.prev
        print(" <-> ".join(elements) if elements else "Empty List")
