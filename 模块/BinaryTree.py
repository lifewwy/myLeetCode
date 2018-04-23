# Python 3.5.2

# 树是数据结构中常用到的一种结构，其实现较栈和队稍为复杂一些。
# 若树中的所有节点的孩子节点数量不超过2个，则该为一个二叉树。
# 二叉树可用于查找和排序等。二叉树的主要操作有：建树，遍历等。
# 遍历是树中的一个最为重要的操作，可分为深度优先遍历和广度优先遍历。
# 其中，尝试优先遍历又可分为先序遍历，中序遍历和后序遍历。
# 深度优先遍历可使用递规来实现，也可以用栈和队通过循环实现。
# 后序的非递规遍历，比其他两种遍历稍为复杂些。
# 下面给出一个python实现二叉树的例子：



class Node(object):
    def __init__(self, data = -1, lchild = None, rchild = None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

class BinaryTree(object):
    def __init__(self):
        self.root = Node()

    def add(self, data):
        node = Node(data)
        if self.isEmpty():
            self.root = node
        else:
            tree_node = self.root
            queue = []
            queue.append(self.root)

            while queue:
                tree_node = queue.pop(0)
                if tree_node.lchild == None:
                    tree_node.lchild = node
                    return
                elif tree_node.rchild == None:
                    tree_node.rchild = node
                    return
                else:
                    queue.append(tree_node.lchild)
                    queue.append(tree_node.rchild)

    def pre_order(self, start):
        node = start
        if node == None:
            return

        print(node.data)
        if node.lchild == None and node.rchild == None:
            return
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    def pre_order_loop(self):
        if self.isEmpty():
            return

        stack = []
        node = self.root
        while node or stack:
            while node:
                print(node.data)
                stack.append(node)
                node = node.lchild
            if stack:
                node = stack.pop()
                node = node.rchild

    def in_order(self, start):
        node = start
        if node == None:
            return
        self.in_order(node.lchild)
        print(node.data)
        self.in_order(node.rchild)

    def in_order_loop(self):
        if self.isEmpty():
            returen

        stack = []
        node = self.root
        while node or stack:
            while node:
                stack.append(node)
                node = node.lchild

            if stack:
                node = stack.pop()
                print(node.data)
                node = node.rchild

    def post_order(self, start):
        node = start
        if node == None:
            return
        self.post_order(node.lchild)
        self.post_order(node.rchild)
        print(node.data)


    def post_order_loop(self):
        if self.isEmpty():
            return

        node = self.root
        stack = []
        queue = []
        queue.append(node)
        while queue:
            node = queue.pop()
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)
            stack.append(node)
        while stack:
            print(stack.pop().data)

    #if lchild and rchild are None or lchild and rchild are printed, print the parent node node and pop out of the stack
    #else lchild and rchild push into the stack
    def post_order_loop1(self):
        if self.isEmpty():
            return

        stack = []
        top = -1
        node = self.root
        stack.append(node)
        #we need to recognize the last printed node
        top += 1
        pre = None
        while stack:
            node = stack[-1]
            if node.lchild is None and node.rchild is None:
                print(node.data)
                pre = node
                top -= 1
            elif not pre and (node.lchild == pre or node.rchild == pre):
                print(node.data)
                pre = node
                top -= 1
            else:
                if node.rchild:
                    if top < len(stack)-1:
                        stack[top] = node.rchild
                    else:
                        stack.append(node.rchild)
                if node.lchild:
                    if top < len(stack)-1:
                        stack[top] = node.lchild
                    else:
                        stack.append(node.lchild)

    def level_order(self):
        node = self.root
        if node == None:
            return

        queue = []
        queue.append(node)

        while queue:
            node = queue.pop(0)
            print(node.data)
            if node.rchild:
                queue.append(node.rchild)
            if node.lchild:
                queue.append(node.lchild)
        print

    def isEmpty(self):
        return True if self.root.data == -1 else False

if __name__ == '__main__':

    arr = [i for i in range(10)]
    print(arr)

    tree = BinaryTree()
    for i in arr:
        tree.add(i)
    print('level_order:')

    tree.level_order()
    print('pre order:')
    tree.pre_order(tree.root)
    print('\npre order loop:')
    tree.pre_order_loop()
    print('\nin_order:')
    tree.in_order(tree.root)
    print('\nin_order loop:')
    tree.in_order_loop()
    print('\npost_order:')
    tree.post_order(tree.root)
    print('\npost_order_loop:')
    tree.post_order_loop()
    print('\npost_order_loop1:')
    tree.post_order_loop1()
