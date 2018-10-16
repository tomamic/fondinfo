#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

class Node:
    def size(self):
        raise NotImplementedError("Abstract method")

    def print(self, indent: int):
        raise NotImplementedError("Abstract method")

class File(Node):
    def __init__(self, name: str, text: str):
        self._name = name
        self._text = text

    def size(self) -> int:
        return len(self._text)

    def print(self, indent: int):
        print(' ' * indent + self._name)

class Folder(Node):
    def __init__(self, name: str):
        self._name = name
        self._subnodes = []

    def add_node(self, n: Node):
        self._subnodes.append(n)

    def size(self) -> int:
        total_size = 0
        for n in self._subnodes:
            total_size += n.size()
        return total_size

    def print(self, indent: int):
        print(' ' * indent + self._name)
        for n in self._subnodes:
            n.print(indent + 4)

def main():
    ball = File('ball.gif', 'an image')
    data = Folder('data')
    data.add_node(ball)
    a1_0 = File('a1.txt', 'bla bla 0')
    cmpt166 = Folder('cmpt166')
    cmpt166.add_node(a1_0)
    cmpt166.add_node(data)
    a1_1 = File('a1.txt', 'a different file')
    macm101 = Folder('macm101')
    macm101.add_node(a1_1)
    desktop = Folder('Desktop')
    desktop.add_node(cmpt166)
    desktop.add_node(macm101)

    print(desktop.size())

    print()
    desktop.print(0)

if __name__ == '__main__':
    main()
