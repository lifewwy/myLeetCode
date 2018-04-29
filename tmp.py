
def println(l):
    print(l.val, end='\t')
    cursor = l.next
    while cursor != None:
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

# head.next, head = head, head.next
head, head.next = head.next, head

println(head)







