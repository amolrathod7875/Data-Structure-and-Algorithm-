from Queue.LC_933.code import RecentCounter


def run_test(pings, expected):
    counter = RecentCounter()
    results = []
    for t in pings:
        results.append(counter.ping(t))

    status = "PASS" if results == expected else "FAIL"
    print(f"{status}: ping({pings})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {results}")
    print()


print("=== LC 933: Number of Recent Calls ===\n")
run_test([1, 100, 3001, 3002], [1, 2, 3, 3])
run_test([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
run_test([3000, 6000, 9000], [1, 2, 2])
run_test([1], [1])
run_test([1, 3001, 6001], [1, 2, 2])
run_test(list(range(1, 11)), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
