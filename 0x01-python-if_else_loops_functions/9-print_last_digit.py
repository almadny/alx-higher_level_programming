#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        rem = (number * -1) % 10
        rem *= -1
    else:
        rem = number % 10
    return rem
    print("{}".format(rem))
