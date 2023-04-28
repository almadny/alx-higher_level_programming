#!/usr/bin/python3
""" Use urllib to send URL Resquest"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    resp = requests.get(url).json()

    if len(resp) < 10:
        limit = len(resp)
    else:
        limit = 10
    for i in range(limit):
        print("{}: {}".format(
                    resp[i].get('sha'),
                    resp[i].get('commit').get('author').get('name'),
                    ))
