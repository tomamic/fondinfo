#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

class Node:
    def size(self):
        raise NotImplementedError("Abstract method")

    def print(self, indent: int):
        raise NotImplementedError("Abstract method")

class Document(Node):
    def __init__(self, name: str, text: str):
        self._name = name
        self._text = text

    def size(self) -> int:
        return len(self._text)

    def print(self, indent: int):
        print(" " * indent + self._name)

class Folder(Node):
    def __init__(self, name: str, subnodes: list[Node]):
        self._name = name
        self._subnodes = subnodes

    def size(self) -> int:
        total_size = 0
        for n in self._subnodes:
            total_size += n.size()
        return total_size

    def print(self, indent: int):
        print(" " * indent + self._name)
        for n in self._subnodes:
            n.print(indent + 4)

def main():
    ball = Document("ball.txt", "spherics")
    data = Folder("data", [ball])
    a1_0 = Document("a1.txt", "bla bla 0")
    cmpt166 = Folder("cmpt166", [a1_0, data])
    a1_1 = Document("a1.txt", "a different file")
    macm101 = Folder("macm101", [a1_1])
    desktop = Folder("Desktop", [cmpt166, macm101])

    print(desktop.size())

    print()
    desktop.print(0)

main()
