#!/usr/bin/python3
""" Use urllib to send URL Resquest"""
import urllib.request
import sys


if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as content:
        header = content.info()

    print("{}".format(header.get('X-Request-Id')))
