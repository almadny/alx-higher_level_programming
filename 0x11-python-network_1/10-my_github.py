#!/usr/bin/python3
""" Use urllib to send URL Resquest"""
import requests
import sys


if __name__ == "__main__":
    u_name = sys.argv[1]
    pwd = sys.argv[2]
    resp = requests.get("https://api.github.com/user", auth=(u_name, pwd))
    rp = resp.json()
    print(rp.get('id'))
