# Author: Aubrey Floyd
# GitHub username: aubreyfloyd2
# Date: 1/30/2023
# Description: Function that takes a positive integer parameter and returns the number
#              at that position of the Fibonacci sequence.

def fib(x):
    """Returns the Fibonacci number at the xth position of the Fibonacci sequence"""
    a = 1
    b = 1
    if x == 1:
        return 1
    if x == 2:
        return 1
    else:
        for i in range(2, x):
            c = a + b
            a = b
            b = c
        return b

# print(fib(17))

