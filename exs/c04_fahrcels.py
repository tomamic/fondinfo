#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

def cels_to_fahr(cels: float) -> float:
    fahr = cels * 1.8 + 32
    return fahr

def main():
    c = float(input("Celsius? "))
    f = cels_to_fahr(c)
    print(f)

main()
