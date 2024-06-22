#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io
@license This software is free - https://opensource.org/license/mit
"""

def palindrome(text: str) -> bool:
    if len(text) <= 1:
        return True
    return text[0] == text[-1] and palindrome(text[1:-1])

if __name__ == "__main__":
    print(palindrome("radar"))
    print(palindrome("tata"))
