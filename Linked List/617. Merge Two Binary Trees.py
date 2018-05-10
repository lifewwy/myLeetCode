# Given two binary trees and imagine that when you put one of them to cover the other,
# some nodes of the two trees are overlapped while the others are not.
#
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap,
#  then sum node values up as the new value of the merged node. Otherwise,
# the NOT null node will be used as the node of new tree.
#
# Example 1:
# Input:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# Output:
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7
# Note: The merging process must start from the root nodes of both trees.

# 题意
#  给定了两个二叉树，要合并成一个树，也就是要将对应节点相加。最后返回即为一个树，对于某一节点，考虑以下三种情况：
#  1）如果给定的节点为空，用其相对应的节点代替它
#  2）如果与其相对应的节点为空，则用这个节点代替二者的和
#  3）如果与其相对应的节点不为空，则将二者加起来，继续考虑该节点的左右子节点，
#  4）考虑树的问题，一般要用到递归。


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 思路：
# 考察的就是二叉树的遍历，遍历每个结点然后如果重叠（两个二叉树结点都不为空）新结点值便为两者和，
# 不重叠（只有一个结点为空）新结点值为不为空的值，全为空到达底部返跳出。按照这个逻辑进行迭代

# 联想：二叉树遍历方式有深度优先和广度优先，深度（纵向）优先在Python中一般使用列表，广度优先（横向）一般使用迭代


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # 结点都为空时
        if t1 is None and t2 is None:
            return

        # 只有一个结点为空时
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        # 结点重叠时
        t1.value += t2.value

        # 进行迭代
        t1.right = self.mergeTrees(t1.right, t2.right)
        t1.left = self.mergeTrees(t1.left, t2.left)

        return t1


if __name__ == '__main__':

    # 用法 https://github.com/joowani/binarytree
    # from binarytree import tree
    # mytree  = tree()
    # print( mytree )

    from binarytree import Node
    # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)
    # root.left.right = Node(4)
    # print( root )

    t1 = Node(1)
    t1.left = Node(3)
    t1.right = Node(2)
    t1.left.left = Node(5)

    t2 = Node(2)
    t2.left = Node(1)
    t2.right = Node(3)
    t2.left.right = Node(4)
    t2.right.right = Node(7)

    print(t1), print(t2)
    print(Solution().mergeTrees(t1,t2))













