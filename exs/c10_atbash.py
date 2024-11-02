#!/usr/bin/env python3
"""
@author  Alberto Ferrari - https://albertoferrari.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import re

_alphabet = "abcdefghijklmnopqrstuvwxyz"
_transform = str.maketrans(_alphabet, _alphabet[::-1])

def encode(s: str) -> str:
    s = re.sub(r"[^a-z]", "", s.lower())
    return s.translate(_transform)
    
def decode(s: str) -> str:
    ds = re.sub(r"[^a-z]", "", s.lower())
    if s != ds:
        raise ValueError("Invalid string")
    return s.translate(_transform)

def encode_simple(txt: str) -> str:
    result = []
    for x in txt.lower():
        if "a" <= x <= "z":
            pos = ord(x) - ord("a")
            result.append(chr(ord("z") - pos))
    return "".join(result)

def main():
    with open("../license.txt", "r") as f, open("_e_license.txt", "w") as e:
        for line in f:
            print(encode_simple(line), file=e)  # or, encode
            
    with open("_e_license.txt", "r") as e:
        for line in e:
            print(encode_simple(line))  # or, decode
            print()

main()
