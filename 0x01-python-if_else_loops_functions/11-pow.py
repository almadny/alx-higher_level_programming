#!/usr/bin/python3
def pow(a, b):
    result = 
    if b < 0:
        b *= -1
        while b > 0:
            result *= a
            b -= 1
        result = 1 / result
    else:
        while b > 0:
            result *= a
            b -= -1 
    return result
