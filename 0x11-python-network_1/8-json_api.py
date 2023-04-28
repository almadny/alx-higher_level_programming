#!/usr/bin/python3
""" Use urllib to send URL Resquest"""
import requests
import sys


if __name__ == "__main__":
    param = {}
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ''
    param['q'] = q
    resp = requests.post("http://0.0.0.0:5000/search_user", data=param)
    try:
        rp = resp.json()
        if len(rp) == 0:
            print("No result")
        else:
            print("[{}] {}".format(rp.get('id'), rp.get('name')))
    except ValueError:
        print("Not a valid JSON")
