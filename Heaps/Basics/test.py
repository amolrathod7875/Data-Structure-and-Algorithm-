from basics import MinHeap, MaxHeap


def run_tests(description, actual, expected):
    status = "Pass" if actual == expected else "fail"
    print(f"{status} : {description}")
    if status == "fail":
        print(f"    Expected: {expected}")
        print(f"    Got: {actual}")
    print()


print("=== MinHeap Tests ===\n")

mh = MinHeap()
mh.insert(10)
mh.insert(20)
mh.insert(5)
mh.insert(30)

run_tests("Peek returns 5 (minimum)", mh.peek(), 5)
run_tests("Extract min returns 5", mh.extract_min(), 5)
run_tests("Extract min returns 10", mh.extract_min(), 10)
run_tests("Size is 2 after two extracts", mh.size(), 2)
run_tests("Extract min returns 20", mh.extract_min(), 20)
run_tests("Extract min returns 30", mh.extract_min(), 30)
run_tests("Heap is empty after all extracts", mh.is_empty(), True)

print("=== MaxHeap Tests ===\n")

mh2 = MaxHeap()
mh2.insert(10)
mh2.insert(20)
mh2.insert(5)
mh2.insert(30)

run_tests("Peek returns 30 (maximum)", mh2.peek(), 30)
run_tests("Extract max returns 30", mh2.extract_max(), 30)
run_tests("Extract max returns 20", mh2.extract_max(), 20)
run_tests("Size is 2 after two extracts", mh2.size(), 2)
run_tests("Extract max returns 10", mh2.extract_max(), 10)
run_tests("Extract max returns 5", mh2.extract_max(), 5)
run_tests("Heap is empty after all extracts", mh2.is_empty(), True)
