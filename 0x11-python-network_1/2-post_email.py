#!/usr/bin/python3
""" Use urllib to send URL Resquest"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    data = {}
    data['email'] = sys.argv[2]
    parameters = urllib.parse.urlencode(data)
    parameters = parameters.encode('ascii')
    request = urllib.request.Request(sys.argv[1], parameters)
    with urllib.request.urlopen(request) as content:
        resp = content.read()

    print("{}".format(resp.decode('utf-8')))
