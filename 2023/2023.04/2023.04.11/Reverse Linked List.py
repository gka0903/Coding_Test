class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)


def reverseList(head):
    while head:
        print(head.val)
        head = head.next

    return 0


print(reverseList(head))
