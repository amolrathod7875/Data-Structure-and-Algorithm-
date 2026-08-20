from Queue.LC_641.code import MyCircularDeque


def run_test(operations, values, expected):
    d = None
    results = []
    for op, val, exp in zip(operations, values, expected):
        if op == "MyCircularDeque":
            d = MyCircularDeque(val[0])
            results.append(None)
        elif op == "insertFront":
            results.append(getattr(d, op)(val[0]))
        elif op == "insertLast":
            results.append(getattr(d, op)(val[0]))
        elif op == "deleteFront":
            results.append(getattr(d, op)())
        elif op == "deleteLast":
            results.append(getattr(d, op)())
        elif op == "getFront":
            results.append(getattr(d, op)())
        elif op == "getRear":
            results.append(getattr(d, op)())
        elif op == "isEmpty":
            results.append(getattr(d, op)())
        elif op == "isFull":
            results.append(getattr(d, op)())

    status = "PASS" if results == expected else "FAIL"
    print(f"{status}: {operations}")
    print(f"  Expected: {expected}")
    print(f"  Got:      {results}")
    print()


print("=== LC 641: Design Circular Deque ===\n")
run_test(
    ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"],
    [[3], [1], [2], [3], [4], [], [], [], [4], []],
    [None, True, True, True, False, 2, True, True, True, 4]
)
run_test(
    ["MyCircularDeque", "insertFront", "deleteLast", "getFront"],
    [[1], [1], [], []],
    [None, True, True, -1]
)
run_test(
    ["MyCircularDeque", "insertLast", "insertFront", "getFront", "getRear", "isEmpty", "isFull", "deleteFront", "deleteLast", "getFront", "getRear"],
    [[2], [1], [2], [], [], [], [], [], [], [], []],
    [None, True, True, 2, 1, False, True, True, True, -1, -1]
)
run_test(
    ["MyCircularDeque", "insertFront", "insertLast", "insertFront", "deleteFront", "getRear", "insertLast", "getFront", "insertFront", "deleteLast", "deleteFront", "getFront"],
    [[3], [1], [2], [3], [], [], [4], [], [5], [], [], []],
    [None, True, True, True, True, 2, True, 1, False, True, True, 2]
)
