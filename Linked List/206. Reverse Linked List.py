

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


# Iterative solution.
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(float("-inf"))
        # dummy = ListNode(0)

        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
            # dummy.next = head
            # head.next = dummy.next
            # head  = head.next
        return dummy.next


if __name__ == "__main__":

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    println(Solution().reverseList(head))











