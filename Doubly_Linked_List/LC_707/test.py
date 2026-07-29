from code import MyLinkedList

l1 = MyLinkedList()


print("=== Initial State ===")
print(f"get(0) : {l1.get(0)}")
print("\n=== addAtHead(1), addAtHead(2) ===")
l1.addAtHead(1)
l1.addAtHead(2)

print(f"get(0) : {l1.get(0)}")
print(f"get(1) : {l1.get(1)}")


print("\n=== addAtTail(3) ===")
l1.addAtTail(3)
print(f"get(2) : {l1.get(2)}")

print("\n=== addAtIndex(1,99) ===")
l1.addAtIndex(1,99)
print(f"get(1) : {l1.get(1)}")
print(f"get(2) : {l1.get(2)}")

print("\n=== deleteAtIndex(1) ===")
l1.deleteAtIndex(1)
print(f"get(0) : {l1.get(0)}")
print(f"get(1) : {l1.get(1)}")
print(f"get(2) : {l1.get(2)}")

print("\n=== Invalid Operations ===")
print(f"get(5) : {l1.get(5)}")
l1.addAtIndex(10,50)
l1.deleteAtIndex(10)
print(f"get(3) : {l1.get(3)}")

print("\n=== Edge case: addAtIndex(0, 0) ===")
l1.addAtIndex(0, 0)
print(f"get(0): {l1.get(0)}")          # 0
print(f"get(1): {l1.get(1)}")