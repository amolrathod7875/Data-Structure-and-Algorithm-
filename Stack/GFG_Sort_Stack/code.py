from typing import Any
class Stack :

    def __init__(self) -> None:
        self.stack : list[Any] = []

    def push(self, value : Any) -> None:
        self.stack.append(value)

    def is_empty(self) -> bool:
        return len(self.stack) == 0 
    
    def pop(self) -> Any :
        if self.is_empty():
            raise IndexError("Stack Underflow")
        return self.stack.pop()

    def __str__(self) -> str:
        return str(self.stack)
    
def SortedInsert(st,x : Any):
    if not st or st[-1] <= x:
        st.append(x)
        return 
    top = st.pop()
    SortedInsert(st,x)
    st.append(top)

def SortStack(st) :
    if not st:
        return 
    top = st.pop()
    SortStack(st)
    SortedInsert(st,top)
        
if __name__ == "__main__":
    st = [41,3,32,2,11]
    print("Original Stack : ", st)
    SortStack(st)
    print(f"Sorted Stack : {st}")