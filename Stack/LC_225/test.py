from Stack.LC_225.code import MyStack


def run_test(operations, values, expected):
    stack = None
    results = []
    for op, val, exp in zip(operations, values, expected):
        if op == "MyStack":
            stack = MyStack()
            results.append(None)
        elif op == "push":
            stack.push(val[0])
            results.append(None)
        elif op == "pop":
            results.append(stack.pop())
        elif op == "top":
            results.append(stack.top())
        elif op == "empty":
            results.append(stack.empty())

    status = "PASS" if results == expected else "FAIL"
    print(f"{status}: {operations}")
    print(f"  Expected: {expected}")
    print(f"  Got:      {results}")
    print()


print("=== LC 225: Implement Stack using Queues ===\n")
run_test(
    ["MyStack", "push", "push", "top", "pop", "empty"],
    [[], [1], [2], [], [], []],
    [None, None, None, 2, 2, False]
)
run_test(
    ["MyStack", "push", "pop", "empty"],
    [[], [1], [], []],
    [None, None, 1, True]
)
run_test(
    ["MyStack", "push", "push", "push", "top", "pop", "top", "pop", "top", "empty", "pop", "empty"],
    [[], [1], [2], [3], [], [], [], [], [], [], [], []],
    [None, None, None, None, 3, 3, 2, 2, 1, False, 1, True]
)
run_test(
    ["MyStack", "empty"],
    [[], []],
    [None, True]
)
