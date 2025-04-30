class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)


def solution(list1, list2):
    prev = dummy = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            prev.next = list1
            list1 = list1.next
        else:
            prev.next = list2
            list2 = list2.next

    while dummy:
        print(dummy.val)
        dummy = dummy.next
    # return dummy.next


print(solution(l1, l2))
