#!/usr/bin/python3
""" Use urllib to send URL Resquest"""
import urllib.request
import sys


if __name__ == "__main__":
    try:
        request = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(request) as content:
            resp = content.read()
            print("{}".format(resp.decode(encoding='utf-8')))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
