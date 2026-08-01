from basics import Queue


def run_tests(description, actual, expected):
    status = "Pass" if actual == expected else "fail"
    print(f"{status} : {description}")
    if status == "fail" :
        print(f"    Expected: {expected}")
        print(f"    Got: {actual}")
    print()
print("=== Queue Tests ===\n")

q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

run_tests(" Dequeue returns 'A'(First Enqueued) ", q.dequeue(), "A")
run_tests("Dequeue returns 'B'", q.dequeue(),"B")
