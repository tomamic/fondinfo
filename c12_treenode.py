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

def contains(tree, val) -> bool:
    if tree == None:
        return False
    if val == tree.data:
        return True
    subtree = tree.left if val < tree.data else tree.right
    return contains(subtree, val)

def flatten(tree) -> list:
    if tree == None:
        return []
    return flatten(tree.left) + [tree.data] + flatten(tree.right)

t = None
for v in [7, 5, 5, 9, 6, 2, 3, 11]:
    t = insert(t, v)
print(t)
print(flatten(t))
print(contains(t, 4))
print(contains(t, 5))
