#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left    # TreeNode | None
        self.right = right  # TreeNode | None

    def __str__(self) -> str:
        return f"<{self.data} {self.left} {self.right}>"

def insert(tree, val) -> TreeNode:
    if tree == None:
        tree = TreeNode(val)
    elif val < tree.data:
        tree.left = insert(tree.left, val)
    elif val > tree.data:
        tree.right = insert(tree.right, val)
    return tree

def postorder_traversal(tree: TreeNode): 
    if tree is not None:
        postorder_traversal(tree.left)  # traverse the left subtree
        postorder_traversal(tree.right)  # traverse the right subtree
        print(tree.data)  # visit the root

t = None
for v in [7, 5, 5, 9, 6, 2, 3, 11]:
    t = insert(t, v)

postorder_traversal(t)


