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


def push_back(node: ListNode, val) -> ListNode:
    if node == None:
        node = ListNode(val)
    else:
        node.next = push_back(node.next, val)
    return node 


def push_front(node: ListNode, val) -> ListNode:
    return ListNode(val, node)


def main():
    l = None
    for v in [0, 1, 1, 2, 3, 5, 8, 13]:
        l = push_back(l, v)
    print(l)

    l = None
    for v in reversed([0, 1, 1, 2, 3, 5, 8, 13]):
        l = push_front(l, v)
    print(l)

if __name__ == "__main__":
    main()