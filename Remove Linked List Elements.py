# Python 3.5.2

import sys
sys.path.append('./模块')  # '.' 表示当前目录
import LinkedList
# ---------------------------------------------------------------------------------------------------------------------
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

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
            if head.data == val:
                return None
            else:
                return head
        else:
            dummy = ListNode(0)
            dummy.next = head
            prev = dummy

            while head != None:
                if head.data == val:
                    prev.next = head.next
                    head = prev

                prev = head
                head = head.next
            return dummy.next


# ---------------------------------------------------------------------------------------------------------------------
if  __name__    ==  "__main__":

    ll = LinkedList.LianBiao()
    for i in [1, 2, 6, 3, 4, 5, 6]:
        ll.addNode(i)
    ll.print()

    s = Solution()
    s.removeElements(ll.root, 6)

    ll.print()









