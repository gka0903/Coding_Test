class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head_node = ListNode(1)
head_node.next = ListNode(2)
head_node.next.next = ListNode(2)
head_node.next.next.next = ListNode(1)


def printNode(node: ListNode):
    crnt_node = node
    while crnt_node:
        print(crnt_node.val, end=' ')
        crnt_node = crnt_node.next


def isPalindrome(head):
    c_node = head
    arr = []
    while c_node:
        arr.append(c_node.val)
        c_node = c_node.next
    arr_reverse = list(reversed(arr))
    return arr == arr_reverse


print(isPalindrome(head_node))
