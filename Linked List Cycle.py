# Python 3.5.2

import sys
sys.path.append('./模块')  # '.' 表示当前目录
import LinkedList
# ---------------------------------------------------------------------------------------------------------------------

# 原题地址：http://oj.leetcode.com/problems/linked-list-cycle/
# 题意：判断链表中是否存在环路。
# 解题思路：快慢指针技巧，slow指针和fast指针开始同时指向头结点head，fast每次走两步，slow每次走一步。
# 如果链表不存在环，那么fast或者fast.next会先到None。
# 如果链表中存在环路，则由于fast指针移动的速度是slow指针移动速度的两倍，
# 所以在进入环路以后，两个指针迟早会相遇，如果在某一时刻slow==fast，说明链表存在环路。

# import webbrowser
# webbrowser.open("http://oj.leetcode.com/problems/linked-list-cycle/")

# Definition for singly-linked list.
# class ListNode(object):
#   def __init__(self, x):
#       self.val = x
#       self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        else:
            fast = head
            slow = head

            while fast != None and fast.next != None:
                slow = slow.next
                fast = fast.next.next
                if fast == slow:
                    break

            if fast == None or fast.next == None:
                return False
            elif fast == slow:
                return True

            return False

# ---------------------------------------------------------------------------------------------------------------------

ll = LinkedList.LianBiao()
for i in range(20):
    ll.addNode(i)
ll.print()

s = Solution()
print( s.hasCycle(ll.root) )

cursor = ll.root
while cursor.next!= None:
    cursor = cursor.next
# print(cursor.data)
# print(cursor.next)

# 制造一个环路
cursor.next = ll.root.next.next.next.next

print( s.hasCycle(ll.root) )


