#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def palindrome(text) -> bool:
    if len(text) <= 1:
        return True
    return text[0] == text[-1] and palindrome(text[1:-1])

if __name__ == '__main__':
    print(palindrome('radar'))
    print(palindrome('tata'))
