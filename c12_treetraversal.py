#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
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

def preorder_traversal(tree: TreeNode):
    if tree is not None:
        print(tree.data)  # visit the root
        preorder_traversal(tree.left)  # traverse the left subtree
        preorder_traversal(tree.right)  # traverse the right subtree

def inorder_traversal(tree: TreeNode):
    if tree is not None:
        inorder_traversal(tree.left)  # traverse the left subtree
        print(tree.data)  # visit the root
        inorder_traversal(tree.right)  # traverse the right subtree

def postorder_traversal(tree: TreeNode):
    if tree is not None:
        postorder_traversal(tree.left)  # traverse the left subtree
        postorder_traversal(tree.right)  # traverse the right subtree
        print(tree.data)  # visit the root

t = None
for v in [7, 5, 5, 9, 6, 2, 3, 11]:
    t = insert(t, v)

print('preorder traversal')
preorder_traversal(t)

print('inorder traversal')
inorder_traversal(t)

print('postorder traversal')
postorder_traversal(t)

