class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


tree = ListNode(1)
for i in range(2, 6):
    cur_node = tree
    while cur_node.next:
        cur_node = cur_node.next
    cur_node.next = ListNode(i)


def solution(t):
    prev = None
    while t:
        if prev is not None:
            p = prev.val
        else:
            p = "none"
        temp = t.next
        t.next = prev
        prev = t
        t = temp

    t = prev
    return 0


print(solution(tree))
