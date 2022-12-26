#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        msg = str[:n] + str[n + 1:]
    else:
        msg = str
    return msg
