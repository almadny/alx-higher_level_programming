#!/usr/bin/python3
def uppercase(str):
    for i in str:
        num = ord(i)
        if num > 96 and num < 123:
            print("{}".format(chr(num - 32)))
        else:
            print("{}".format(chr(num)))
