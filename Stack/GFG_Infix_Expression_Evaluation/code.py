import math 
from typing import Any, List


def isNumber(token : str) -> bool :
    if not token :
        return False
    start = 1 if token[0] == "-" else 0
    if start == 1 and len(token) == 1 :
        return False
    for ch in token[start:]:
        if not ch.isdigit():
            return False
    return True

def precedence(op : str) -> int :
    if op == "+" or op == "-":
        return 1
    if op == "*" or op == "/":
        return 2
    if op == "^":
        return 3
    return 0

def isRightAssociative(op : str) -> bool :
    return op == "^"

def applyOperation(a : int, b : int, op : str) -> Any:
    if op == "+" : return a + b 
    if op == "-" : return a - b 
    if op == "*" : return a * b 
    if op == "/" : return a // b
    if op == "^" : return math.pow(a,b)
    return 0 

def evaluateInfix(arr):
    values = []
    ops = []
    n = len(arr)
    for i in range(n):
        token = arr[i]

        if isNumber(token):
            values.append(int(token))
        else:
            while ops and (
                (precedence(ops[-1]) > precedence(token)) 
                or (precedence(ops[-1]) == precedence(token))
                and not isRightAssociative(token)
            ) :
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(applyOperation(val1,val2,op))
            ops.append(token)
    while ops:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.append(applyOperation(val1, val2, op))
    return values[0]
if __name__ == "__main__":
    arr = ["2", "^", "3", "^", "2"]
    print(evaluateInfix(arr))