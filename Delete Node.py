# Python 3.5.2

import sys
sys.path.append('./模块')  # '.' 表示当前目录
import LinkedList
# ---------------------------------------------------------------------------------------------------------------------

# Write a function to delete a node (except the tail) in a singly linked list,
# given only access to that node.
# Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with
# value 3, the linked list should become 1 -> 2 -> 4 after calling your function.
# URL: https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.data = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place
        instead.
        """
        if node == None:
            pass
        else:
            next_node = node.next
            node.data = next_node.data
            node.next = next_node.next

if __name__ == '__main__':
    ll = LinkedList.LianBiao()
    for i in range(1,5):
        ll.addNode(i)
    ll.print()

    s = Solution()
    s.deleteNode(ll.root.next.next)
    # rtype: void Do not return anything, modify node in-place

    ll.print()






