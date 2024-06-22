#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next  # ListNode | None

    def __str__(self) -> str:
        return f"<{self.data} {self.next}>"


class Stack:
    def __init__(self):
        self._node = None

    def push(self, val):
        self._node = ListNode(val, self._node)

    def pop(self):
        if self.empty():
            raise ValueError("Empty stack")
        val = self._node.data
        self._node = self._node.next
        return val

    def empty(self):
        return not self._node

    def __str__(self) -> str:
        return str(self._node)

def main():
    s = Stack()
    for v in [0, 1, 1, 2, 3, 5, 8, 13]:
        s.push(v)
    print(s)

    while not s.empty():
        print(s.pop())  # Last-In First-Out

if __name__ == "__main__":
    main()
