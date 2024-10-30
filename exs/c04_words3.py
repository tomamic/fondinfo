#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

def words3(alphabet: str) -> list[str]:
    for c in alphabet:
        if alphabet.count(c) > 1:
            raise ValueError(f"Reapeated char ({c})")

    result = []
    for c1 in alphabet:
        for c2 in alphabet:
            for c3 in alphabet:
                word = c1 + c2 + c3
                result.append(word)
    return result

def main():
    alphabet = input("alphabet? ")
    print(words3(alphabet))

if __name__ == "__main__":
    main()
