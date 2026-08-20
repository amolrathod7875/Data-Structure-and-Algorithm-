from code import ListNode, Solution


def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def run_test(values, left, right, expected):
    head = build_list(values)
    sol = Solution()
    result = sol.reverseBetween(head, left, right)
    actual = to_list(result)
    status = "PASS" if actual == expected else "FAIL"
    print(f"{status}: reverseBetween({values}, {left}, {right})")
    print(f"  Expected: {expected}")
    print(f"  Got:      {actual}")
    print()


if __name__ == "__main__":
    run_test([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5])
    run_test([1, 2, 3, 4, 5], 1, 5, [5, 4, 3, 2, 1])
    run_test([1, 2, 3], 2, 2, [1, 2, 3])
    run_test([1], 1, 1, [1])
    run_test([1, 2], 1, 2, [2, 1])
    run_test([1, 2, 3, 4, 5], 1, 3, [3, 2, 1, 4, 5])
    run_test([1, 2, 3, 4, 5], 3, 5, [1, 2, 5, 4, 3])