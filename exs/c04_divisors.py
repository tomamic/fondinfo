#!/usr/bin/env python3
"""
@author  Alberto Ferrari - https://albertoferrari.github.io/
@license This software is free - https://opensource.org/license/mit
"""

def common_divisors(num1, num2):
    divisors = []
    # Find the smaller number between num1 and num2
    smaller = min(num1, num2)
    # Iterate from 1 to the smaller number
    for i in range(1, smaller + 1):
        # If both numbers are divisible by i ...
        if num1 % i == 0 and num2 % i == 0:
            divisors.append(i)
    return divisors

# Test the function
num1 = 12
num2 = 18
print("Common divisors of", num1, "and", num2, ":")
print(common_divisors(num1, num2))
