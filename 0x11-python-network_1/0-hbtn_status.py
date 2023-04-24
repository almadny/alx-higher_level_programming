#!/usr/bin/python3
""" Use urllib to send URL Resquest"""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(request) as content:
        cont = content.read()

    print("Body response:")
    print("    - type: {}".format(type(cont)))
    print("    - content: {}".format(cont))
    print("    - utf8 content: {}".format(cont.decode(encoding='utf-8')))
