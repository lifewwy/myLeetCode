

def println(l):
    print(l.val, end='\t')
    cursor = l.next
    while cursor != None:
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
            # head.next, dummy.next, head = dummy.next, head, head.next
            # head.next, head, dummy.next= dummy.next, head.next, head

            # 为什么换成下面这句就不对了 ？？？？？？？？
            # head 与 head.next 的次序不能交换
            # head, dummy.next, head.next = head.next, head, dummy.next
            # dummy.next, head, head.next = head, head.next, dummy.next


        return dummy.next


    # def reverseList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     dummy = ListNode(None)
    #     while head:  # 终止条件是head=Null
    #         nextnode = head.next  # nextnode是head后面的节点
    #         head.next = dummy.next  # dummy.next是Null，所以这样head.next就成为了Null
    #         dummy.next = head  # head当前数字给dummy.next
    #         head = nextnode  # head向后一位
    #     return dummy.next


if __name__ == "__main__":

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    println(Solution().reverseList(head))











