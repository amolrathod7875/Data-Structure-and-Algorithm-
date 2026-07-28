from doubly_linked_list import DoublyLinkedList, Node

print("=== Test 1: Basic Append and Display ===")
dll = DoublyLinkedList()
for i in range(1,6):
    dll.append(i)
print('Forward : ', end=' ')
dll.display_forward()
print('Backword : ',end=' ')
dll.display_backword()

print("\n=== Test 2: Remove Middle Node ===")
node3 = dll.head.next.next
dll.remove_node(node3)
print("After Removing 3 : ", end=' ')
dll.display_forward()

print("\n=== Test 3: Remove Head ===")
dll.remove_node(dll.head)
print("After Removing Head : ", end= " ")
dll.display_forward()


print("\n=== Test 4: Remove Tail ===")
dll.remove_node(dll.tail)
print("After Removing Tail : ", end= " ")
dll.display_forward()

print("\n=== Test 5: Insert New Node Before Existing ===")
dll2 = DoublyLinkedList()
for i in range(1,4):
    dll2.append(i)
print("Original : ",end=" ")
dll2.display_forward()
node2 = dll2.head.next
new_node = Node(99)
dll2.insert_before(new_node,node2)
print("After inserting 99 before 2 : ", end=' ')
dll2.display_forward()

print("\n=== Test 6 : Move Existing Node to new Location ===")
dll3 = DoublyLinkedList()
n1 = dll3.append(1)
n2 = dll3.append(2)
n3 = dll3.append(3)
n4 = dll3.append(4)
n5 = dll3.append(5)
print('Original : ', end=' ')
dll3.display_forward()
dll3.insert_before(n2, n4)
print('After moving 2 before 4: ', end=' ')
dll3.display_forward()
print("Backward : ", end=' ')
dll3.display_backword()