class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head_node = ListNode(1)
head_node.next = ListNode(2)
head_node.next.next = ListNode(2)
head_node.next.next.next = head_node


def hasCycle(head) -> bool:
    slow = fast = head
    while fast:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


print(hasCycle(head_node))
