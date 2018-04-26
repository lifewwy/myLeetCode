

class Solution(object):
    def __init__(self, l):
        print(l.val, end='\t')
        cursor = l.next
        while cursor != None:
            print(cursor.val, end='\t')
            cursor = cursor.next
        print()

# # Definition for singly-linked list.
# class ListNode(object):
#   def __init__(self, x):
#       self.val = x
#       self.next = None
#
#
# if  __name__    ==  "__main__":
#
#     ll = ListNode(6);
#     ll.next = ListNode(2);
#     ll.next.next = ListNode(6);
#     ll.next.next.next = ListNode(3);
#     ll.next.next.next.next = ListNode(4);
#     ll.next.next.next.next.next = ListNode(5);
#     ll.next.next.next.next.next.next = ListNode(6);
#
#     println(ll)