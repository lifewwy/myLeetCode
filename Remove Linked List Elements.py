# Python 3.5.2
# ---------------------------------------------------------------------------------------------------------------------
def println(l):
    print(l.val, end='\t')
    cursor = l.next
    while cursor!=None:
        print(cursor.val, end='\t')
        cursor = cursor.next
    print()

# ---------------------------------------------------------------------------------------------------------------------
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


#          |--- val
#  ListNode|                    |--- val
#          |--- next -> ListNode|                    |--- val
#                               |--- next -> ListNode|
#                                                    |--- next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
        elif head != None and head.next == None:
            if head.val == val:
                return None
            else:
                return head
        else:
            dummy = ListNode(0)
            dummy.next = head
            prev = dummy

            while head != None:
                if head.val == val:
                    prev.next = head.next
                    head = prev

                prev = head
                head = head.next
            return dummy.next


# ---------------------------------------------------------------------------------------------------------------------
if  __name__    ==  "__main__":

    ll = ListNode(6);
    ll.next = ListNode(2);
    ll.next.next = ListNode(6);
    ll.next.next.next = ListNode(3);
    ll.next.next.next.next = ListNode(4);
    ll.next.next.next.next.next = ListNode(5);
    ll.next.next.next.next.next.next = ListNode(6);


    println(ll)


    s = Solution()
    ll = s.removeElements(ll, 6)

    println(ll)












