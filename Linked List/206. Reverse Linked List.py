

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

        return dummy.next

# Recursive solution.
class Solution2:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        [begin, end] = self.reverseListRecu(head)
        return begin

    def reverseListRecu(self, head):
        if not head:
            return [None, None]

        [begin, end] = self.reverseListRecu(head.next)

        if end:
            end.next = head
            head.next = None
            return [begin, head]
        else:
            return [head, head]

if __name__ == "__main__":

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    println(Solution2().reverseList(head))












