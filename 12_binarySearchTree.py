import numpy as np

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def in_order_tree_walk(self):
        if self:
            if self.left:
                self.left.in_order_tree_walk()
            else:
                print str(self.key)+" has no left child"
            print self.key
            if self.right:
                self.right.in_order_tree_walk()
            else:
                print str(self.key)+" has no right child"

class BST:
    def __init__(self):
        self.root = None

    def set_root(self, key):
        self.root = Node(key)

    def insert_node(self, subroot, key):
        if key <= subroot.key:
            if subroot.left:
                self.insert_node(subroot.left, key)
            else:
                subroot.left = Node(key)
        elif key > subroot.key:
            if subroot.right:
                self.insert_node(subroot.right, key)
            else:
                subroot.right = Node(key)

    def insert(self, key):
        if self.root is None:
            self.set_root(key)
        else:
            self.insert_node(self.root, key)

T = BST()
A = range(63)
np.random.shuffle(A)
for i in A:
    T.insert(i)
R = T.root
R.in_order_tree_walk()




