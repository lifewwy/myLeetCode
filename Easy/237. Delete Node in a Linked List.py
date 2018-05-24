# 题目翻译
# 写个函数删除一个单链表中的一个节点（非尾节点），该函数的参数是要删除的节点。
# 比如一个链表是 1 -> 2 -> 3 -> 4 ， 给你一个值为3的节点，调用你的函数后链表变成 1 -> 2 -> 4 。

# 思路方法
# 这是一个非常简单的单链表的题，稍微拐了一点弯。
# 一般删除一个节点是通过上一个节点来操作，
# 现在只给了当前节点，那么只能将后一节点的值赋给当前节点，将后一节点删掉，则相当于删掉了“当前节点”。

# ---------------------------------------------------------------------------------------------------------------------

def println(l):
    print(l.val, end='\t')
    cursor = l.next
    while cursor != None:
        print(cursor.val, end='\t')
        cursor = cursor.next
    print()

# ---------------------------------------------------------------------------------------------------------------------

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    l = ListNode(1);
    l.next = ListNode(2);
    l.next.next = ListNode(3);
    l.next.next.next = ListNode(4);

    println(l)

    s = Solution()
    s.deleteNode(l.next.next)

    println(l)









