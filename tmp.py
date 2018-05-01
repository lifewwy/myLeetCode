def println(l, N = 10):
    if not l:
        return

    print(l.val, end='\t')
    cursor = l.next
    nCount = 1
    while cursor != None and nCount < N:
        nCount += 1
        print(cursor.val, end='\t')
        cursor = cursor.next
    print()

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def a(head):
    println(head)

    if not head:
        return

    a(head.next)

    println(head)


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

a(head)
