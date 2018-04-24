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





# 分析：
#
# 1. 对于链表，在删除当前节点时，需要知道当前节点的父节点。
#
# 2. 对于非头节点，删除操作很方便，对于头节点需要额外的操作，为了在遍历的过程中，
#    保持删除操作的一致性和避免区分头节点和非头节点，有两种方法来避免这种麻烦：
#
# ① 可以为链表设置辅助头节点（即在原来链表前插入头节点），这样对具有辅助头节点的链表，
#    在遍历时就不存在区分头节点和非头节点的问题。
#
# The key to solve this problem is using a helper node to track the head of the list.
#
# ② 从头节点的下一个节点开始遍历查找删除，遍历完成后再处理头节点。






