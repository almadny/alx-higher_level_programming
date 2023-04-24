#!/usr/bin/python3
""" Use urllib to send URL Resquest"""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(request) as content:
        cont = content.read()
    print("Body response: \n\t - type: {}\n\t - content: {}\n\t
          - utf - 8 content: {}"
          .format(type(cont), cont, cont.decode(encoding='utf-8')))
