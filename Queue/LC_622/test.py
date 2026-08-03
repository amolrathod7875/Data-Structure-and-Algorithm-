from Queue.LC_622.code import MyCircularQueue


def run_test(operations, values, expected):
    q = None
    results = []
    for op, val, exp in zip(operations, values, expected):
        if op == "MyCircularQueue":
            q = MyCircularQueue(val[0])
            results.append(None)
        elif op == "enQueue":
            results.append(getattr(q, op)(val[0]))
        elif op == "deQueue":
            results.append(getattr(q, op)())
        elif op == "Front":
            results.append(getattr(q, op)())
        elif op == "Rear":
            results.append(getattr(q, op)())
        elif op == "isEmpty":
            results.append(getattr(q, op)())
        elif op == "isFull":
            results.append(getattr(q, op)())

    status = "PASS" if results == expected else "FAIL"
    print(f"{status}: {operations}")
    print(f"  Expected: {expected}")
    print(f"  Got:      {results}")
    print()


print("=== LC 622: Design Circular Queue ===\n")
run_test(
    ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"],
    [[3], [1], [2], [3], [4], [], [], [], [4], []],
    [None, True, True, True, False, 3, True, True, True, 4]
)
run_test(
    ["MyCircularQueue", "enQueue", "deQueue", "Front", "deQueue", "Front", "Rear", "enQueue", "isFull", "Rear"],
    [[2], [1], [], [], [], [], [], [2], [], []],
    [None, True, True, -1, False, -1, -1, True, False, 2]
)
run_test(
    ["MyCircularQueue", "enQueue", "enQueue", "deQueue", "enQueue", "deQueue", "enQueue", "deQueue", "enQueue", "deQueue", "Front", "Rear"],
    [[3], [1], [2], [], [3], [], [4], [], [5], [], [], []],
    [None, True, True, True, True, True, True, True, True, True, 5, 5]
)
run_test(
    ["MyCircularQueue", "enQueue", "deQueue", "enQueue", "Front", "Rear"],
    [[1], [1], [], [2], [], []],
    [None, True, True, True, 2, 2]
)
