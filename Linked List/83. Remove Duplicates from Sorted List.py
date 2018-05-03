# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Example 1:
# Input: 1->1->2
# Output: 1->2

# Example 2:
# Input: 1->1->2->3->3
# Output: 1->2->3

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


def ListToLink(x):
    l = ListNode(88)
    p = l
    N = len(x)
    for i in range(N):
        p.next = ListNode(x[i])
        p = p.next
    return l.next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        while p:
            if p.next and p.next.val == p.val:
                p.next = p.next.next
            else:
                p = p.next
        return head


if __name__ == "__main__":

    l = ListNode(1)
    l.next = ListNode(1)
    l.next.next = ListNode(1)
    l.next.next.next = ListNode(5)

    print(Solution().deleteDuplicates(l))

    l1 = ListToLink([1, 2, 4, 4, 6, 6, 6, 8])
    print(Solution().deleteDuplicates(l1))