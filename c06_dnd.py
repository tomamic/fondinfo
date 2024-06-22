#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from random import randint

class DnDCharacter:
    def __init__(self, name: str):
        self._name = name
        self._hp = randint(15, 30)  # hit points

    def hit(self, damage: int) -> None:
        self._hp = max(self._hp - damage, 0)

    def heal(self, cure: int) -> None:
        if (self.alive()):
            self._hp = min(self._hp + cure, 30)

    def alive(self) -> bool:
        return self._hp > 0

    def describe(self) -> str:
        return f"I’m {self._name}. I have {self._hp} hit points."


def main():
    c = DnDCharacter("Hero")
    print(c.describe())

    for _ in range(3):
        c.hit(randint(5, 10))
        print(c.describe())

    c.heal(randint(5, 10))
    print(c.describe())

    print(c.alive())


if __name__ == "__main__":
    main()
