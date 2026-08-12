from typing import Any

class Stack:
    def __init__(self) -> None :
        self.stack : list[Any] = []

    def push(self,values : Any ) -> None :
        self.stack.append(values)

    def is_empty(self) -> bool :
        return len(self.stack) == 0 

    def pop(self) -> Any:
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Stack is Empty")

    def __str__(self) -> str:
        return str(self.stack) 

def insert_at_bottom(stack, item):

    if stack.is_empty():
        stack.push(item)
        return 

    top = stack.pop()
    insert_at_bottom(stack,item)
    stack.push(top)
        

def reverse_stack(stack):
    if stack.is_empty():
        return

    top = stack.pop() 
    reverse_stack(stack)
    insert_at_bottom(stack, top)

if __name__ == "__main__":
    st = Stack()
    for val in [1,5,6,8,9] :
        st.push(val)
    print(f"Original Stack : {st}")

    reverse_stack(st)

    print(f"Reversed Stack : {st}")
