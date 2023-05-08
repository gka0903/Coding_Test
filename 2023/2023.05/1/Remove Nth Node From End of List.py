class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


tree = ListNode(1)
tree.next = ListNode(2)
tree.next.next = ListNode(3)
tree.next.next.next = ListNode(4)
tree.next.next.next.next = ListNode(5)
count = 1
while tree:
    count += 1
    if count == n:
        t
