from Queue.LC_346.code import MovingAverage


def run_test(size, inputs, expected):
    ma = MovingAverage(size)
    results = []
    for val in inputs:
        results.append(round(ma.next(val), 5))

    status = "PASS" if results == expected else "FAIL"
    print(f"{status}: next({inputs}) with size={size}")
    print(f"  Expected: {expected}")
    print(f"  Got:      {results}")
    print()


print("=== LC 346: Moving Average from Data Stream ===\n")
run_test(3, [1, 10, 3, 5], [1.0, 5.5, 4.66667, 6.0])
run_test(1, [1, 2, 3], [1.0, 2.0, 3.0])
run_test(2, [1, 2, 3], [1.0, 1.5, 2.5])
run_test(3, [1, 2, 3, 4, 5], [1.0, 1.5, 2.0, 3.0, 4.0])
run_test(4, [-1, -2, -3, -4, -5], [-1.0, -1.5, -2.0, -2.5, -3.5])
run_test(2, [100, 200, 300], [100.0, 150.0, 250.0])
