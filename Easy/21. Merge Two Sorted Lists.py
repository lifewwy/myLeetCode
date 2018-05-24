
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

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

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

# ①②③④⑤⑥⑦⑧⑨↖↑↗←→↙↓↘

class Solution(object):
    def mergeTwoLists(self, l1, l2):       # curr   l1① → ③ → ④
                                           #  ⑧
        # :type l1: ListNode               # dummy  l2② → ⑤
        # :type l2: ListNode               ---------------------------
        # :rtype: ListNode
                                           #        curr① → l1③ → ④
        curr = dummy = ListNode(8)         #  ⑧   ↗
        while l1 and l2:                   # dummy  l2② → ⑤
            if l1.val < l2.val:            # --------------------------
                curr.next = l1
                l1 = l1.next               #        ①  l1③ → ④
            else:                          #  ⑧   ↗ ↓
                curr.next = l2             # dummy  curr② → l2⑤
                l2 = l2.next               # --------------------------
            curr = curr.next
        curr.next = l1 or l2               #        ①  curr③ → l1④
        return dummy.next                  #  ⑧   ↗ ↓ ↗
                                           # dummy  ②  l2⑤



if __name__ == "__main__":

    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(4)

    l2 = ListNode(2)
    l2.next = ListNode(5)

    l = Solution().mergeTwoLists(l1,l2)

    print( l )
    # println( l )