#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next  # ListNode | None

    def __str__(self) -> str:
        return f"<{self.data} {self.next}>"


def insert(node: ListNode, val) -> ListNode:
    if node == None:
        node = ListNode(val)
    else:
        node.next = insert(node.next, val)
    return node 


l = None
for v in [0, 1, 1, 2, 3, 5, 8, 13]:
    l = insert(l, v)
print(l)
