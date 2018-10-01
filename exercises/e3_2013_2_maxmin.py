#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def max_min(filename: str) -> (int, int):
    with open(filename, "r") as f:
        first_line = True
        min_val, max_val = 0.0, 0.0
        for line in f:
            val = float(line)
            if val > max_val or first_line:
                max_val = val
            if val < min_val or first_line:
                min_val = val
            first_line = False
    return max_val, min_val

def main():
    fn = input("filename? ")
    mx, mn = max_min(fn)
    print(mx, mn)

if __name__ == "__main__":
    main()
