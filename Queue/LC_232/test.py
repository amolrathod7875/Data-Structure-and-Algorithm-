from Queue.LC_232.code import MyQueue


def run_test(operations, values, expected):
    q = None
    results = []
    for op, val, exp in zip(operations, values, expected):
        if op == "MyQueue":
            q = MyQueue()
            results.append(None)
        elif op == "push":
            getattr(q, op)(val)
            results.append(None)
        elif op == "pop":
            results.append(getattr(q, op)())
        elif op == "peek":
            results.append(getattr(q, op)())
        elif op == "empty":
            results.append(getattr(q, op)())

    status = "PASS" if results == expected else "FAIL"
    print(f"{status}: {operations}")
    print(f"  Expected: {expected}")
    print(f"  Got:      {results}")
    print()


print("=== LC 232: Implement Queue using Stacks ===\n")
run_test(
    ["MyQueue", "push", "push", "peek", "pop", "empty"],
    [[], [1], [2], [], [], []],
    [None, None, None, 1, 1, False]
)
run_test(
    ["MyQueue", "push", "push", "pop", "pop", "empty"],
    [[], [1], [2], [], [], []],
    [None, None, None, 1, 2, True]
)
run_test(
    ["MyQueue", "push", "push", "peek", "push", "pop", "peek", "pop", "empty"],
    [[], [1], [2], [], [3], [], [], [], []],
    [None, None, None, 1, None, 1, 2, 3, False]
)
run_test(
    ["MyQueue", "empty"],
    [[], []],
    [None, True]
)
