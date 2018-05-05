# Python 3.5.2

# ---------------------------------------------------------------------------------------------------------------------
# import sys
# sys.path.append('./模块')  # '.' 表示当前目录

# import LinkedList

# ---------------------------------------------------------------------------------------------------------------------

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
class ListNode(object):
  def __init__(self, x):
      self.val = x
      self.next = None

  def __repr__(self):
      if self:
          return "{} → {}".format(self.val, self.next)


#          |--- val
#  ListNode|                    |--- val
#          |--- next -> ListNode|                    |--- val
#                               |--- next -> ListNode|
#                                                    |--- next


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # 解法 ①
        if head == None or head.next == None:
            return False

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

        # 解法 ②

# ---------------------------------------------------------------------------------------------------------------------


if  __name__    ==  "__main__":

    ll = ListNode(6);
    ll.next = ListNode(2);
    ll.next.next = ListNode(6);
    ll.next.next.next = ListNode(3);
    ll.next.next.next.next = ListNode(4);
    ll.next.next.next.next.next = ListNode(5);
    ll.next.next.next.next.next.next = ListNode(6);


    print(ll)

    s = Solution()
    print('链表中是否存在环路：', s.hasCycle(ll) )

    # 制造一个环路
    ll.next.next.next.next.next.next.next = ll.next.next;

    println(ll,10)

    print('链表中是否存在环路：', s.hasCycle(ll) )





