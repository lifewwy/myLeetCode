
def println(l, N = 10):
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


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

println(head)


print('head的地址：', id(head))
print('head.next的地址：', id(head.next))


# head.next, head = head, head.next
# head, head.next = head.next, head


print('head的地址：', id(head))
print('head.next的地址：', id(head.next))

println(head)














